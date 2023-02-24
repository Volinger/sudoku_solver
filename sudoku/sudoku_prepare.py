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

    def __init__(self):
        self.sudoku = None
        self.available_for_removal = None
        self.removed_all_numbers = False

    def generate(self, seed):
        self.sudoku = Sudoku()
        Sudoku.generate_grid(seed)
        self.available_for_removal = np.ndarray(np.ndindex(self.sudoku.grid.shape), dtype=bool)
        self.available_for_removal.fill(True)

    def prepare(self, difficulty, seed):
        sudoku = self.generate(seed)
        self.difficulty_select(difficulty)
        self.remove_numbers()
        return sudoku.grid

    def remove_numbers(self, difficulty):
        for x in range(difficulty):
            removed = self.remove_random_number()
            if not removed:
                self.removed_all_numbers = True
                break

    def remove_random_number(self):
        while True:
            position = np.random.choice(np.ndindex(self.available_for_removal.shape)[self.available_for_removal])
            self.sudoku.grid[position] = 0
            solvable = self.sudoku.check_solvable()
            self.available_for_removal[position] = False
            if solvable:
                return True
            elif any(self.available_for_removal):
                continue
            else:
                return False

    def check_solvable(self):
        while True:
            if (position := self.sudoku.check_next_single_option_position()) != -1:
                self.sudoku.fill_single_choice(position)
            elif self.sudoku.check_next_single_option_position == -1:
                if any(self.sudoku.grid == 0):
                    return True
            else:
                return False
