"""
Sudoku API
"""

from sudoku.sudoku_core import SudokuCore
from sudoku.sudoku_prepare import SudokuPreparer
from sudoku.sudoku_generator import SudokuGenerator
import sudoku.exceptions as exceptions


class SudokuHandler:
	"""
	Main class intended to handle API requests.
	"""
	def __init__(self):
		self.completed_grid = None
		self.sudoku = None
		self.user_grid = None

	def generate(self, size: int=9, seed: int=None):
		"""
		Generate sudoku object
		:param size: Sudoku grid size, can be 4,9,16... Note: sizes larger than 16 are not recommended.
		:param seed: Leave empty for random sudoku, or specify if you wish to have reproducible generation.
		:return:
		"""
		generator = SudokuGenerator(size=size)
		generator.generate_grid(seed=seed)
		self.sudoku = generator.sudoku
		self.completed_grid = generator.sudoku.grid

	def prepare_for_solving(self, cells_to_remove: int):
		"""
		Prepare sudoku so it can be solved by randomly removing specified number of cells. Guarantees that sudoku
		will be still solvable. if the specified cells_to_remove is too high and would cause sudoku to be unsolvable,
		it will remove only as many cells as possible.
		possible.
		:param cells_to_remove: Number of cells which will be removed from completed sudoku.
		:return:
		"""
		if self.sudoku is not None:
			preparer = SudokuPreparer(sudoku=self.sudoku)
			self.sudoku = preparer.prepare(cells_to_remove=cells_to_remove)
			self.user_grid = self.sudoku.grid
		else:
			raise exceptions.GenerationException('Sudoku was not generated yet. Call .generate() before this method')

	def get_completed_grid(self):
		"""
		return completed sudoku grid
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
		solved = sudoku.solve()
		if solved:
			self.completed_grid = sudoku.grid
		else:
			raise exceptions.UnsolvableException("Could not solve selected sudoku.")
