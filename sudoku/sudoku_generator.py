"""
Handles generation of sudoku puzzle.
"""

import numpy as np
import sudoku.sudoku as sudoku


class SudokuGenerator:
    """
    class for handling sudoku generation.
    """
    def __init__(self, size):
        """

        :param size: int, defines size of sudoku grid, i.e. 4 for numbers 1-4, 9 for numbers 1-9 etc.
        """
        self.sudoku = sudoku.Sudoku(size=size)
        # self.total_size = size #size of sudoku = total_size * total_size, can be 4,9,16...
        # self.grid = np.zeros((self.total_size, self.total_size), dtype=int)
        # self.cell_size = int(self.total_size**0.5)
        # self.init_possible_numbers()
        self.number_selection_memory = []
        self.number_selection_random = []
        self.rollbacked_filter = np.ndarray((self.sudoku.get_size(), self.sudoku.get_size(), self.sudoku.get_size()),
                                            dtype=bool)
        self.rollbacked_filter.fill(True)

    # def init_possible_numbers(self):
    #     self.possible_numbers = np.ndarray((self.total_size, self.total_size, self.total_size), dtype=bool)
    #     self.possible_numbers.fill(True)

    def get_allowed_numbers(self):
        """
        Allowed numbers are combination of possible numbers (which filters numbers by the sudoku rules) and rollbacked
        filter (which filters numbers based on rollbacks done through generation process).
        :return:
        """
        return np.multiply(self.sudoku.possible_numbers, self.rollbacked_filter)

    def generate_grid(self, seed=50):
        """
        Main method for puzzle generation.
        :param seed: int => seed for numpy random function
        :return: 2d np array with sudoku values
        """
        np.random.seed(seed)
        while self.sudoku.any_free_position():
            self.randomly_fill_next_position()
            while True:
                if self.check_no_options():
                    self.rollback_last_random()
                    break
                elif (position := self.check_next_single_option_position()) != -1:
                    self.fill_single_choice(position)
                else:
                    break

    def check_no_options(self):
        """
        Check if there are any positions, which do not have any allowed number which could be assigned to them.
        :return:
        """
        empty_positions = self.sudoku.get_empty_positions()
        positions_without_options = np.ndarray((self.sudoku.get_size(), self.sudoku.get_size()), dtype=bool)
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
                self.rollbacked_filter[last_random_position, previous_value] = False
                self.reset_dependent_rollbacks(last_random_position)
                break

    def reset_dependent_rollbacks(self, max_position):
        """
        When rollback is applied and there are some positions which were previously banned because they failed to
        produce solvable sudoku further in the line, reset them.
        :param max_position:
        :return:
        """
        positions = np.ndindex(self.rollbacked_filter.shape[:2])
        positions_filtered = []
        for position in reversed(list(positions)):
            if position == max_position:
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
        if not next_position == -1:
            options = np.arange(1, self.sudoku.get_size()+1)
            allowed_mask = self.get_allowed_numbers()[next_position]
            allowed_options = options[allowed_mask]
            choice = np.random.choice(allowed_options)
            self.sudoku.update_position(position=next_position, value=choice)
            self.number_selection_memory.append(next_position)
            self.number_selection_random.append(True)

    # def get_next_free_position(self):
    #     """
    #     Return next grid position with no number assigned.
    #     :return:
    #     """
    #     for position in np.ndindex(self.grid.shape):
    #         if self.grid[position] == 0:
    #             return position
    #     return -1

    def check_next_single_option_position(self):
        """
        Scan grid for next position, which has only 1 number available as option.
        :return: coords (x, y) or -1 if not found
        """
        for position in np.ndindex(self.get_allowed_numbers().shape[:2]):
            if sum(self.get_allowed_numbers()[position]) == 1 and self.sudoku.get_position(position) == 0:
                return position
        return -1

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

    # def check_next_single_option_position(self):
    #     """
    #     Scan grid for next position, which has only 1 number available as option.
    #     :return: coords (x, y) or -1 if not found
    #     """
    #     for position in np.ndindex(self.get_allowed_numbers().shape[:2]):
    #         if sum(self.get_allowed_numbers()[position]) == 1 and self.grid[position] == 0:
    #             return position
    #     return -1
    #
    # def fill_position(self, position, number):
    #     self.grid[position] = number
    #
    # def reset_possible_numbers(self):
    #     """
    #     Re-generate possible numbers based on grid contents
    #     :return:
    #     """
    #     self.init_possible_numbers()
    #     for position in np.ndindex(self.grid.shape):
    #         if self.grid[position] != 0:
    #             self.update_options_single_number(position, self.grid[position])
    #
    # def update_options_single_number(self, position, number):
    #     """
    #     Update possible numbers for positions based on sudoku rules.
    #     :param position: tuple(x, y)
    #     :param number: int
    #     :return:
    #     """
    #     self.update_row(position[0], number)
    #     self.update_column(position[1], number)
    #     self.update_cell(position, number)
    #
    # def update_row(self, row, number):
    #     """
    #     Update possible numbers based on sudoku rule which allows only one number of a kind in a row.
    #     :param row:
    #     :param number:
    #     :return:
    #     """
    #     self.possible_numbers[row, :, number-1] = False
    #
    # def update_column(self, column, number):
    #     """
    #     Update possible numbers based on sudoku rule which allows only one number of a kind in a column.
    #     :param column:
    #     :param number:
    #     :return:
    #     """
    #     self.possible_numbers[:, column, number-1] = False
    #
    # def update_cell(self, position, number):
    #     """
    #     Update possible numbers based on sudoku rule which allows only one number of a kind in a cell.
    #     :param position:
    #     :param number:
    #     :return:
    #     """
    #     cell_x = (position[0] // self.cell_size) * self.cell_size
    #     cell_y = (position[1] // self.cell_size) * self.cell_size
    #     self.possible_numbers[cell_x:cell_x + self.cell_size, cell_y:cell_y + self.cell_size, number-1] = False