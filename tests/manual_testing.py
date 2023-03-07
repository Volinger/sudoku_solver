from sudoku.sudoku_handler import SudokuHandler

handler = SudokuHandler()
handler.generate(size=3)
sudoku = handler.get_grid()
print(sudoku)
