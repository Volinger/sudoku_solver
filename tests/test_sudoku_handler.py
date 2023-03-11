import pytest
import numpy as np
import sudoku.sudoku_handler as sudoku_handler
import sudoku.sudoku_generator as sudoku_generator
import sudoku.sudoku_prepare as sudoku_prepare

@pytest.fixture
def handler():
	return sudoku_handler.SudokuHandler()


class TestSudokuHandler:

	def test_check_user_position(self, handler):
		handler.generate(size=4, seed=50)
		handler.prepare_for_solving(difficulty=15)
		handler.user_grid[0, 2] = 4
		match = handler.check_user_position((0, 2))
		mismatch = handler.check_user_position((1, 0))
		assert match and not mismatch

	def test_generate(self, handler):
		handler.generate(size=4, seed=50)
		expected = np.asarray([[1, 2, 4, 3],
							   [4, 3, 2, 1],
							   [2, 1, 3, 4],
							   [3, 4, 1, 2]])
		assert (expected == handler.completed_grid).all()

	def test_prepare_for_solving(self, handler):
		handler.generate(size=4, seed=50)
		handler.prepare_for_solving(difficulty=15)
		expected = [[1, 2, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 2]]
		assert (expected == handler.sudoku.grid).all()

	def test_put_user_number(self, handler):
		handler.generate(size=4)
		handler.prepare_for_solving(difficulty=5)
		handler.put_user_number(position=[0, 1], number=5)
		assert handler.user_grid[0, 1] == 5

	def test_reset(self, handler):
		handler.generate(size=4)
		handler.prepare_for_solving(difficulty=10)
		handler.user_grid[0, 1] = 999
		handler.reset()
		assert (handler.user_grid == handler.sudoku.grid).all()

	def test_solve_grid(self, handler):
		generator = sudoku_generator.SudokuGenerator(size=4)
		generator.generate_grid()
		grid = generator.sudoku.grid
		preparer = sudoku_prepare.SudokuPreparer(sudoku=generator.sudoku)
		preparer.prepare(difficulty=15)
		handler.solve_grid(preparer.sudoku.grid)
		assert (handler.completed_grid == grid).all()
