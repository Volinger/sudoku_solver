"""
Handles preparation of sudoku for solving.
"""
import numpy as np
from enum import IntEnum


class Difficulty(IntEnum):
    easy = 10
    medium = 20
    hard = 30


class SudokuPreparer:

    def __init__(self, sudoku):
        self.available_for_removal = None
        self.removed_all_numbers = False
        self.sudoku = sudoku
        self.available_for_removal = np.ndarray((self.sudoku.get_size(), ) * 2, dtype=bool)
        self.available_for_removal.fill(True)

    def prepare(self, cells_to_remove):
        """
        Prepare solved sudoku for solving by removing amount of numbers from grid based on difficulty.
        :param difficulty:
        :return:
        """
        self.remove_numbers(cells_to_remove)
        return self.sudoku

    def remove_numbers(self, cells_to_remove):
        """
        Remove numbers in sudoku grid, until either required number of removals is reached, or no more numbers can be
        removed without making sudoku unsolvable.
        :param difficulty:
        :return:
        """
        for x in range(cells_to_remove):
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
            solvable = self.sudoku.attempt_to_solve()
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

