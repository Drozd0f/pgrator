import os
import asyncio
from argparse import ArgumentParser

from migrator.src.db import make_migration


def main():
    ap = ArgumentParser(description='Module for migrate postgres database')
    ap.add_argument('-p', '--path', default=os.environ.get('MIGRATOR_MIGRATIONS_PATH'),
                    required=True, help='Path to migrations')
    ap.add_argument('-d', '--db-uri', default=os.environ.get('MIGRATOR_DB_URI'),
                    required=True, help='URI for connect to database')
    args = ap.parse_args()
    asyncio.run(make_migration(args.path, args.db_uri))


if __name__ == '__main__':
    main()
