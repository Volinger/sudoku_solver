from sudoku.sudoku_handler import SudokuHandler

handler = SudokuHandler()
handler.generate(size=3)
handler.prepare_for_solving(size=3, difficulty=3)
sudoku = handler.prepared_sudoku
print(sudoku)
sudoku = handler.get_result()
print(sudoku)
