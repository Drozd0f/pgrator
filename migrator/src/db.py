import logging
import typing as t
from pathlib import Path

import asyncpg
from asyncpg import Connection

from migrator.src.utils import parse_migration_number, get_migration_paths


QUERIES_DIR = Path(Path(__file__).parent.parent / 'queries/pathlib')
DB_CONNECTION: t.Optional[asyncpg.Connection] = None
log = logging.getLogger(__name__)


def get_query(query_name: str, query_path: Path) -> t.Optional[str]:
    with open(f'{query_path.with_name(query_name)}.sql', 'r') as query:
        return query.read()


async def init_migration_table(conn: Connection):
    await conn.execute(get_query('init', QUERIES_DIR))
    if await get_current_version(conn) is None:
        await conn.execute(get_query('create_base_value', QUERIES_DIR))


async def get_current_version(conn: Connection) -> int:
    return await conn.fetchval(get_query('get_current_version', QUERIES_DIR))


async def update_migration_schema(current_version: int, is_dirt: bool, conn: Connection):
    await conn.execute(
        get_query('update_migration_schema', QUERIES_DIR),
        current_version, is_dirt
    )


async def apply_migration(migration_name: str, migration_path: Path, conn: Connection):
    await conn.execute(get_query(migration_name, migration_path))


async def make_migration(path: str, db_uri: str):
    conn: Connection = await asyncpg.connect(db_uri)
    await init_migration_table(conn)
    migrations_path = get_migration_paths(path)
    current_version = await get_current_version(conn)
    is_dirt = False
    try:
        for migrate_path in migrations_path:
            migration_version = parse_migration_number(migrate_path.stem)
            if migration_version > current_version:
                current_version = migration_version
                await apply_migration(migrate_path.stem, migrate_path, conn)
    except Exception as e:
        is_dirt = True
        raise e
    finally:
        await update_migration_schema(current_version, is_dirt, conn)
