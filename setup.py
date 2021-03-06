import glob
from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


def sql_file_picker(directorie: str) -> list[tuple[str, list[str]]]:
    return [('queries', glob.glob(directorie + '/*.sql'))]


setup(
    name='pgrate',
    description='Package for applying migrations to the postgresql database',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Drozd0f, qerdcv',
    author_email='danylo.drozdov@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    packages=['migrator', 'migrator.src'],
    data_files=sql_file_picker('migrator/queries'),
    include_package_data=True,
    install_requires=[
        'asyncpg==0.25.0'
    ],
    entry_points={
        'console_scripts': [
            'pgrate=migrator.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    project_urls={
        'Homepage': 'https://github.com/Drozd0f/migrator',
        'Bug Tracker': 'https://github.com/Drozd0f/migrator/issues'
    }
)
