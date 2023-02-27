"""
Handles preparation of sudoku for solving.
"""
import numpy as np

from sudoku.sudoku_generator import SudokuGenerator
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
        self.sudoku = SudokuGenerator(size)
        self.sudoku.generate_grid(seed)
        self.available_for_removal = np.ndarray((self.sudoku.total_size, self.sudoku.total_size), dtype=bool)
        self.available_for_removal.fill(True)

    def prepare(self, difficulty):
        """
        Prepare solved sudoku for solving by removing amount of numbers from grid based on difficulty.
        :param difficulty:
        :return:
        """
        self.remove_numbers(difficulty)
        return self.sudoku.grid

    def remove_numbers(self, difficulty: Difficulty):
        """
        Remove numbers in sudoku grid, until either required number of removals is reached, or no more numbers can be
        removed without making sudoku unsolvable.
        :param difficulty:
        :return:
        """
        for x in range(difficulty):
            removed = self.remove_random_number()
            if not removed:
                self.removed_all_numbers = True
                break

    def remove_random_number(self):
        """
        Select random position in sudoku and remove number from it, as long as this allows sudoku to be still solvable.
        If not, rollback removal and attempt to remove other number randomly. Return true if number was successfully
        removed. In case that all the options were exhausted and still no number was removed, return False.
        case that all options are
        exhausted,
        :return:
        """
        while True:
            random_position = self.select_random_filled_position()
            previous_value = self.sudoku.grid[random_position]
            self.sudoku.grid[random_position] = 0
            solvable = self.check_solvable()
            self.available_for_removal[random_position] = False
            if solvable:
                return True
            elif self.available_for_removal.any():
                self.sudoku.grid[random_position] = previous_value
                continue
            else:
                self.sudoku.grid[random_position] = previous_value
                return False

    def select_random_filled_position(self):
        nonzero_indices = np.nonzero(self.sudoku.grid)
        nonzero_positions = np.array(list(zip(nonzero_indices[0], nonzero_indices[1])))
        random_index = np.random.choice(len(nonzero_positions))
        random_position = tuple(nonzero_positions[random_index])
        return random_position

    def check_solvable(self):
        """
        Attempt to solve sudoku. Returns True if it is possible to solve it based on implemented solving steps.
        :return:
        """
        self.sudoku.reset_possible_numbers()
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
