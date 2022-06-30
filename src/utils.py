import re
from pathlib import Path


def parse_migration_number(name_migrate: str) -> int:
    return int(re.findall(r'\d+', name_migrate)[0])


def get_migration_paths(path: str) -> list[Path]:
    return sorted(list(Path(path).glob('[0-9]*_*.up.sql')))
