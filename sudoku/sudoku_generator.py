"""
Handles generation of sudoku puzzle.
"""

import numpy as np
import sudoku.sudoku_core as sudoku_core


class SudokuGenerator:
    """
    class for handling sudoku generation.
    """
    def __init__(self, size):
        """

        :param size: int, defines size of sudoku grid, i.e. 4 for numbers 1-4, 9 for numbers 1-9 etc.
        """
        self.sudoku = sudoku_core.SudokuCore()
        self.sudoku.init(size=size)
        self.number_selection_memory = []
        self.number_selection_random = []
        self.rollbacked_filter = np.ndarray((self.sudoku.get_size(), ) * 3, dtype=bool)
        self.rollbacked_filter.fill(True)

    def get_allowed_numbers(self):
        """
        Allowed numbers are combination of possible numbers (which filters numbers by the sudoku rules) and rollbacked
        filter (which filters numbers based on rollbacks done through generation process).
        :return:
        """
        return np.multiply(self.sudoku.possible_numbers, self.rollbacked_filter)

    def generate_grid(self, seed=None):
        """
        Main method for puzzle generation.
        :param seed: int => seed for numpy random function.
        :return: 2d np array with sudoku values
        """
        if seed is not None:
            np.random.seed(seed)
        while self.sudoku.any_free_position():
            self.randomly_fill_next_position()
            while True:
                if self.check_no_options():
                    self.rollback_last_random()
                elif (position := self.check_next_single_option_position()) is not None:
                    self.fill_single_choice(position)
                else:
                    break

    def get_sudoku(self):
        return self.sudoku

    def check_no_options(self):
        """
        Check if there are any positions, which do not have any allowed number which could be assigned to them.
        :return:
        """
        empty_positions = self.sudoku.get_empty_positions()
        positions_without_options = np.ndarray((self.sudoku.get_size(), ) * 2, dtype=bool)
        for position in np.ndindex(self.get_allowed_numbers().shape[:2]):
            positions_without_options[position] = not any(self.get_allowed_numbers()[position])
        empty_without_options = np.logical_and(empty_positions, positions_without_options)
        return np.any(empty_without_options)

    def rollback_last_random(self):
        """
        Loop through selection memory in backwards direction and remove all options, until one which was selected
        randomly was removed as well.
        :return:
        """
        for random_indicator in reversed(self.number_selection_random):
            last_random_position = self.number_selection_memory.pop()
            self.number_selection_random.pop()
            previous_value = self.sudoku.get_position(last_random_position)
            self.sudoku.clean_position(position=last_random_position)
            if random_indicator:
                rollback_index = list(last_random_position)
                rollback_index.insert(2, previous_value-1)
                rollback_index = tuple(rollback_index)
                self.rollbacked_filter[rollback_index] = False
                self.reset_dependent_rollbacks(last_random_position)
                break

    def reset_dependent_rollbacks(self, rollbacked_position):
        """
        When rollback is applied and there are some positions which were previously banned because they failed to
        produce solvable sudoku further in the line, reset them.
        :param max_position:
        :return:
        """
        positions = np.ndindex(self.rollbacked_filter.shape[:2])
        positions_filtered = []
        for position in reversed(list(positions)):
            if position == rollbacked_position:
                break
            positions_filtered.append(position)
        for position in positions_filtered:
            self.rollbacked_filter[position] = True

    def randomly_fill_next_position(self):
        """
        Select randomly number which is allowed and put it to sudoku grid.
        :return:
        """
        next_position = self.sudoku.get_next_free_position()
        if next_position is not None:
            options = np.arange(1, self.sudoku.get_size()+1)
            allowed_mask = self.get_allowed_numbers()[next_position]
            allowed_options = options[allowed_mask]
            choice = np.random.choice(allowed_options)
            self.sudoku.fill_position(position=next_position, value=choice)
            self.number_selection_memory.append(next_position)
            self.number_selection_random.append(True)

    def check_next_single_option_position(self):
        """
        Scan grid for next position, which has only 1 number available as option.
        :return: coords (x, y) or None if not found
        """
        for position in np.ndindex(self.get_allowed_numbers().shape[:2]):
            if sum(self.get_allowed_numbers()[position]) == 1 and self.sudoku.get_position(position) == 0:
                return position
        return None

    def fill_single_choice(self, position):
        """
        Used for positions which have only one possible number.
        :param position:
        :return:
        """
        single_option_value = np.where(self.get_allowed_numbers()[position])[0] + 1
        self.sudoku.fill_position(position, single_option_value)
        self.number_selection_memory.append(position)
        self.number_selection_random.append(False)
