"""
Sudoku API
"""

from sudoku.sudoku import Sudoku
from sudoku.sudoku_prepare import SudokuPreparer
from sudoku.sudoku_generator import SudokuGenerator


class SudokuHandler:

	def __init__(self):
		self.completed_sudoku = None
		self.prepared_sudoku = None
		self.user_grid = None

	def generate(self, size):
		"""
		generate sudoku object
		:return:
		"""
		generator = SudokuGenerator(size=size)
		generator.generate_grid()
		self.completed_sudoku = generator.sudoku

	def prepare_for_solving(self, size, difficulty):
		"""
		prepare sudoku so it can be solved
		:return:
		"""
		preparer = SudokuPreparer(size=size, seed=50)
		self.prepared_sudoku = preparer.prepare(difficulty)
		self.user_grid = self.prepared_sudoku.grid

	def solve(self):
		"""
		Solve sudoku from loaded grid. Returns solved sudoku.
		:return:
		"""
		sudoku = Sudoku.from_grid()
		sudoku.solve()
		return sudoku.grid

	def get_grid(self):
		"""
		return sudoku grid
		:return:
		"""
		return self.completed_sudoku.grid

	def solve_single(self):
		"""
		solves single position if possible
		:return:
		"""
		pass

	def reset(self):
		"""
		resets sudoku to original state before user stared solving
		:return:
		"""
		self.user_grid = self.sudoku.grid

	def put_user_number(self, position, number):
		"""
		puts number by the user into grid
		:return:
		"""
		self.user_grid[position] = number
		pass

	def check_user_position(self, position):
		"""
		checks if number put by user is correct
		:return:
		"""
		return self.sudoku.grid[position] == self.user_grid[position]

	def solve_grid(self, grid):
		"""
		Creates sudoku object from supplied grid and solves it if possible.
		:return:
		"""
		sudoku = Sudoku()
		sudoku.from_grid(grid)
		sudoku.solve()
		self.completed_sudoku = sudoku.grid

	def get_result(self):
		"""
		Get completed solution of sudoku.
		:return:
		"""
		return self.completed_sudoku
