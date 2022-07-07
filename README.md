# Package for applying migrations to the postgresql database

[![Lint](https://github.com/Drozd0f/migrator/actions/workflows/linter.yml/badge.svg)](https://github.com/Drozd0f/migrator/actions/workflows/linter.yml)

Not for production purposes.

Tool to migrate database from files.

## **Install**

```shell
$ pip install pgrate
```

## **Usage**

```shell
pgrate -p directorie/to/migrations -d postgres://username:password@localhost:5432/database
```

**OR**

```shell
pgrate -p directorie/to/migrations -d postgresql://username:password@localhost:5432/database
```

> **NOTE**
> Migration name must starts with a number + "_", where number is migration version and ends with *.up.sql example (001_migration_name.up.slq)

## **Examples**

* Move into working directory and create default migrations folder

```shell
$ cd /path/to/project
$ mkdir migrations
```

* Creating a migration up and down

```sql
-- migrations/001_init.up.sql
CREATE TABLE IF NOT EXISTS users(
  id serial PRIMARY KEY, 
  name VARCHAR(255)
);
```

```sql
-- migrations/001_init.down.sql
DROP TABLE IF EXISTS users;
```

* Applying migrations

```shell
$ pgrate -p ./migrations -d postgres://username:password@localhost:5432/database
```

* Results

**Migration schema**

| current_version | is_dirt |
|:---------------:|:-------:|
|        1        |  false  |

* Creating a migration up and down with error

```sql
-- migrations/002_users.up.sql
CREATE TABLE users(
  id serial PRIMARY KEY, 
  name VARCHAR(255)
);
```

```sql
-- migrations/002_users.down.sql
DROP TABLE IF EXISTS users;
```

* Applying migrations

```shell
$ pgrate -p ./migrations -d postgres://username:password@localhost:5432/database
```

* Results

**Console log**

```shell
asyncpg.exceptions.DuplicateTableError: relation "users" already exists
```

**Migration schema**

| current_version | is_dirt |
|:---------------:|:-------:|
|        2        |   true  |

## Commands

|      Command     |         Description         |
|:----------------:|:---------------------------:|
| '-p'<br>'--path'   | Path to migrations folder |
| '-d'<br>'--db-uri' | Database connection URI   |
