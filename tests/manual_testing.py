from sudoku.sudoku_prepare import SudokuPreparer
from sudoku.sudoku_generator import SudokuGenerator

x = SudokuGenerator(size=9)
x.generate_grid(seed=0)
print(x.sudoku.grid)

# prep = SudokuPreparer(size=16, seed=50)
# sudoku = prep.prepare(difficulty=70)
# print(sudoku)
