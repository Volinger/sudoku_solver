from sudoku.sudoku_handler import SudokuHandler

handler = SudokuHandler()
handler.generate(size=3)
handler.prepare_for_solving(difficulty=3)
sudoku = handler.sudoku
print(sudoku)
sudoku = handler.get_grid()
print(sudoku)
