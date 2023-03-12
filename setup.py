from setuptools import setup
from pathlib import Path

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='Sudoku-py-lib',
    version='1.0.8',
    packages=['sudoku'],
    url='',
    license='Apache 2.0',
    author='Vollinger',
    author_email='',
    description='package to generate and solve sudoku puzzles',
    install_requires=['numpy==1.24.2'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
