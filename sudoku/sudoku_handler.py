"""
Handles sudoku operations
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

	def prepare_for_solving(self, difficulty):
		"""
		prepare sudoku so it can be solved
		:return:
		"""
		preparer = SudokuPreparer()
		self.prepared_sudoku = preparer.prepare(difficulty)
		self.user_grid = self.sudoku.grid

	def solve(self):
		self.sudoku.solve()

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

	def to_file(self, file):
		"""
		Writes generated sudoku to file
		:return:
		"""
		with open(file) as f:
			f.write(self.completed_sudoku)
