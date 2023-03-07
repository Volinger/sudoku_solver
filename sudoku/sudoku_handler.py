"""
Handles sudoku operations
"""

from sudoku.sudoku import Sudoku


class SudokuHandler:

	def __init__(self):
		self.sudoku = Sudoku()

	def generate(self):
		"""
		generate sudoku object
		:return:
		"""
		pass

	def prepare_for_solving(self):
		"""
		prepare sudoku so it can be solved
		:return:
		"""
		pass

	def solve(self):
		"""
		solve sudoku in a given state if possoble
		:return:
		"""
		pass

	def get_grid(self):
		"""
		return sudoku grid
		:return:
		"""
		pass

	def single(self):
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
		pass

	def put_user_number(self):
		"""
		puts number by the user into grid
		:return:
		"""
		pass

	def revert_user_number(self):
		"""
		reverts number previously filled by the user
		:return:
		"""
		pass

	def check_user_number(self):
		"""
		checks if number put by user is correct
		:return:
		"""
		pass