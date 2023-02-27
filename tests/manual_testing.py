from sudoku.sudoku_prepare import SudokuPreparer

# x = Sudoku(size=4)
# x.generate_grid(seed=50)
# print(x.grid)

prep = SudokuPreparer(size=9, seed=50)
sudoku = prep.prepare(difficulty=70)
print(sudoku)
