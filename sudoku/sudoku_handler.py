"""
Sudoku API
"""

from sudoku.sudoku import Sudoku
from sudoku.sudoku_prepare import SudokuPreparer
from sudoku.sudoku_generator import SudokuGenerator


class SudokuHandler:

	def __init__(self):
		self.completed_grid = None
		self.sudoku = None
		self.user_grid = None

	def generate(self, size):
		"""
		generate sudoku object
		:return:
		"""
		generator = SudokuGenerator(size=size)
		generator.generate_grid()
		self.sudoku = generator.sudoku
		self.completed_grid = generator.sudoku.grid

	def prepare_for_solving(self, difficulty):
		"""
		prepare sudoku so it can be solved
		:return:
		"""
		preparer = SudokuPreparer(sudoku=self.sudoku)
		self.sudoku = preparer.prepare(difficulty=difficulty)
		self.user_grid = self.sudoku.grid

	def get_grid(self):
		"""
		return sudoku grid
		:return:
		"""
		return self.completed_grid.grid

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

	def solve_grid(self, grid):
		"""
		Creates sudoku object from supplied grid and solves it if possible.
		:return:
		"""
		sudoku = Sudoku()
		sudoku.from_grid(grid)
		sudoku.solve()
		self.completed_grid = sudoku.grid
