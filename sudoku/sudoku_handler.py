"""
Sudoku API
"""

from sudoku.sudoku_core import SudokuCore
from sudoku.sudoku_prepare import SudokuPreparer
from sudoku.sudoku_generator import SudokuGenerator


class SudokuHandler:

	def __init__(self):
		self.completed_grid = None
		self.sudoku = None
		self.user_grid = None

	def generate(self, size=9, seed=None):
		"""
		generate sudoku object
		:return:
		"""
		generator = SudokuGenerator(size=size)
		generator.generate_grid(seed=seed)
		self.sudoku = generator.sudoku
		self.completed_grid = generator.sudoku.grid

	def prepare_for_solving(self, cells_to_remove):
		"""
		prepare sudoku so it can be solved
		:return:
		"""
		preparer = SudokuPreparer(sudoku=self.sudoku)
		self.sudoku = preparer.prepare(cells_to_remove=cells_to_remove)
		self.user_grid = self.sudoku.grid

	def get_grid(self):
		"""
		return sudoku grid
		:return:
		"""
		return self.completed_grid

	def get_puzzle(self):
		"""
		Output prepared puzzle as 2D list
		:return:
		"""
		return self.sudoku.grid.tolist()

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
		return self.completed_grid[position] == self.user_grid[position]

	def solve_grid(self, grid: list):
		"""
		Creates sudoku object from supplied grid and solves it if possible.
		:return:
		"""
		sudoku = SudokuCore()
		sudoku.from_grid(grid)
		sudoku.solve()
		self.completed_grid = sudoku.grid
