import asyncio
import logging
import typing as t

import asyncpg


DB_CONNECTION: t.Optional[asyncpg.Connection] = None
log = logging.getLogger(__name__)


def get_query(query_path: str) -> t.Optional[str]:
    with open(query_path, 'r') as query:
        return query.read()


def db_connection(db_uri: str) -> asyncpg.Connection:
    global DB_CONNECTION
    if DB_CONNECTION is None:
        DB_CONNECTION = asyncio.run(asyncpg.connect(db_uri))
    return DB_CONNECTION


async def init_migration_table():
    raise NotImplementedError('creating a table. 2 columns: current_version and is_dirty')


async def check_vers_migration(conn):
    raise NotImplementedError('checking in the database column with the version for the latest version number')


async def applying_migration(conn):
    raise NotImplementedError('applying migrations')


async def make_migration(path: str, db_uri: str):
    await db_connection(db_uri).execute(
        get_query(path)
    )
