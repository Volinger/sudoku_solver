from sudoku.sudoku_generator import Sudoku

x = Sudoku(size=4)
x.generate_grid(seed=50)
print(x.grid)