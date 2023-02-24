"""
Handles preparation of sudoku for solving.
"""
import numpy as np

from sudoku.sudoku_generator import Sudoku
from enum import IntEnum

class Difficulty(IntEnum):
    easy = 10
    medium = 20
    hard = 30


class SudokuPreparer:

    def __init__(self, size, seed):
        self.sudoku = None
        self.available_for_removal = None
        self.removed_all_numbers = False
        self.sudoku = Sudoku(size)
        self.sudoku.generate_grid(seed)
        self.available_for_removal = np.ndarray((self.sudoku.total_size, self.sudoku.total_size), dtype=bool)
        self.available_for_removal.fill(True)

    def prepare(self, difficulty):
        self.remove_numbers(difficulty)
        return self.sudoku.grid

    def remove_numbers(self, difficulty: Difficulty):
        for x in range(difficulty):
            removed = self.remove_random_number()
            if not removed:
                self.removed_all_numbers = True
                break

    def remove_random_number(self):
        while True:
            nonzero_indices = np.nonzero(self.sudoku.grid)
            positions = np.array(list(zip(nonzero_indices[0], nonzero_indices[1])))
            ndx = np.random.choice(len(positions))
            position = tuple(positions[ndx])
            previous_value = self.sudoku.grid[position]
            self.sudoku.grid[position] = 0
            solvable = self.check_solvable()
            self.available_for_removal[position] = False
            if solvable:
                return True
            elif self.available_for_removal.any():
                self.sudoku.grid[position] = previous_value
                continue
            else:
                self.sudoku.grid[position] = previous_value
                return False

    def check_solvable(self):
        self.sudoku.reset_available_options()
        original_grid = self.sudoku.grid.copy()
        while True:
            if (position := self.sudoku.check_next_single_option_position()) != -1:
                self.sudoku.fill_single_choice(position)
            elif self.sudoku.check_next_single_option_position() == -1:
                if (self.sudoku.grid == 0).any():
                    self.sudoku.grid = original_grid
                    return False
                else:
                    self.sudoku.grid = original_grid
                    return True
