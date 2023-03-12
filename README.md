
# Sudoku-py-lib: create sudoku puzzles

 Sudoku-py-lib is a Python package that allows creation of sudoku puzzles from scratch.

 

## Features

- Generation of random sudoku puzzles
- Solving of puzzles
- Uploading custom puzzle grids



## Installation

Package is located on PyPI: https://pypi.org/project/Sudoku-py-lib/

You can download and install sudoku-py-lib with pip:

```bash
  pip install sudoku-py-lib
```
    
## Dependencies

    numpy==1.24.2
## Usage/Examples
#### Creating puzzle
```python
from sudoku import SudokuHandler 

sudoku_handler = SudokuHandler()  # Initialize handler object
sudoku_handler.generate()   # Generate new completed sudoku
sudoku_handler.prepare_for_solving(cells_to_remove=10)  # Prepare sudoku for solving by removing specified amount of cells.

print(sudoku_handler.get_puzzle())  # Returns prepared sudoku as 2D list
```

#### Solve existing puzzle

```python
from sudoku import SudokuHandler 

sudoku_handler = SudokuHandler()  # Initialize handler object
sudoku_handler.solve_grid(grid)   # Processes sudoku grid and solves it.

print(sudoku_handler.completed_grid  # Returns completed sudoku as 2D list
```
