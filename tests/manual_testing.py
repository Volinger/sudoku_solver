import sudoku


handler = sudoku.SudokuHandler()
# handler.generate(size=4)
# handler.prepare_for_solving(cells_to_remove=50)
# sudoku = handler.sudoku
# print(sudoku)
# sudoku = handler.get_completed_grid()
# print(sudoku)

handler.solve_grid([[1, 2, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 4, 0, 2]])
print(handler.get_completed_grid())
