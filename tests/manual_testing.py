from sudoku.sudoku_prepare import SudokuPreparer
from sudoku.sudoku_generator import SudokuGenerator

x = SudokuGenerator(size=4)
x.generate_grid(seed=50)
print(x.sudoku.grid)

# prep = SudokuPreparer(size=9, seed=50)
# sudoku = prep.prepare(difficulty=70)
# print(sudoku)
