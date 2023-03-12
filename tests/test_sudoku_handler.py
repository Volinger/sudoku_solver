import pytest
import numpy as np
import sudoku.sudoku_handler as sudoku_handler
import sudoku.sudoku_generator as sudoku_generator
import sudoku.sudoku_prepare as sudoku_prepare


@pytest.fixture
def handler():
	handler = sudoku_handler.SudokuHandler()
	handler.generate(size=4, seed=50)
	return handler


@pytest.fixture
def prepared_handler(handler):
	handler.prepare_for_solving(cells_to_remove=10)
	return handler


@pytest.fixture
def prepared_grid():
	return [[1, 2, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 4, 0, 2]]


@pytest.fixture
def completed_grid():
	return [[1, 2, 4, 3], [4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2]]


class TestSudokuHandler:

	def test_check_user_position(self, prepared_handler):
		prepared_handler.user_grid[0, 2] = 4
		match = prepared_handler.check_user_position((0, 2))
		mismatch = prepared_handler.check_user_position((1, 0))
		assert match and not mismatch

	def test_generate(self, handler, completed_grid):
		expected = np.asarray(completed_grid)
		assert (expected == handler.completed_grid).all()

	def test_prepare_for_solving(self, prepared_handler, prepared_grid):
		expected = prepared_grid
		assert (expected == prepared_handler.sudoku.grid).all()

	def test_put_user_number(self, handler):
		handler.prepare_for_solving(cells_to_remove=5)
		handler.put_user_number(position=[0, 1], number=5)
		assert handler.user_grid[0, 1] == 5

	def test_reset(self, prepared_handler):
		prepared_handler.user_grid[0, 1] = 999
		prepared_handler.reset()
		assert (prepared_handler.user_grid == prepared_handler.sudoku.grid).all()

	def test_solve_grid(self, handler):
		generator = sudoku_generator.SudokuGenerator(size=4)
		generator.generate_grid()
		grid = generator.sudoku.grid
		preparer = sudoku_prepare.SudokuPreparer(sudoku=generator.sudoku)
		preparer.prepare(cells_to_remove=10)
		handler.solve_grid(preparer.sudoku.grid)
		assert (handler.completed_grid == grid).all()

	def test_get_puzzle(self, prepared_handler, prepared_grid):
		expected = prepared_grid
		assert prepared_handler.get_puzzle() == expected
