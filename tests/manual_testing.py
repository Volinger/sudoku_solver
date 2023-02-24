from sudoku_generator.sudoku_generator import Sudoku

x = Sudoku(size=9)
x.generate_grid(seed=55)
print(x.grid)