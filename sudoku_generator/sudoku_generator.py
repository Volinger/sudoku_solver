import numpy as np

class Sudoku:

    def __init__(self, size):
        self.total_size = size #size of sudoku = total_size * total_size, can be 2,4,9
        self.grid = np.zeros((self.total_size, self.total_size), dtype=int)
        self.cell_size = int(self.total_size**0.5)
        self.possible_numbers = np.ndarray((self.total_size, self.total_size, self.total_size), dtype=bool)
        self.possible_numbers.fill(True)
        self.number_selection_memory = []
        self.number_selection_random = []

    def generate_grid(self):
        np.random.seed(50)
        while any(self.grid == 0):
            self.randomly_fill_next_position()
            while True:
                single_position = self.check_next_single_option_position()
                if single_position != -1:
                    self.fill_single_choice()
                else:
                    break

    def check_no_options(self):
        empty_positions = self.grid == 0
        positions_without_options = np.ndarray((self.total_size, self.total_size), dtype=bool)
        for position in np.ndindex(self.possible_numbers.shape[:2]):
            positions_without_options[position] = not any(self.possible_numbers[(position)])
        empty_without_options = np.logical_and(empty_positions, positions_without_options)
        return np.any(empty_without_options)

    def rollback_last_random(self):
        pass

    def randomly_fill_next_position(self):
        next_position = self.get_next_free_position()
        if not next_position == (-1, -1):
            available_options = self.grid[next_position]
            choice = np.random.choice(available_options)
            self.grid[self.next_position] = choice
            self.number_selection_memory.append(next_position)
            self.number_selection_random.append(True)

    def fill_single_choice(self, position):
        single_option_value = np.where(self.possible_numbers[position])[0] + 1
        self.fill_position(position, single_option_value)

    def check_next_single_option_position(self):
        for position in np.ndindex(self.possible_numbers.shape[:2]):
            if sum(self.possible_numbers[position]) == 1:
                return position
        return -1

    def fill_position(self, position, number):
        self.grid[position] = number

    def reset_available_options(self):
        for position in self.number_selection_memory:
            self.update_options_single_number(position, self.grid[position])

    def update_options_single_number(self, position, number):
        self.update_row(position[0], number)
        self.update_column(position[1], number)
        self.update_cell(position, number)

    def update_row(self, row, number):
        self.possible_numbers[row, :, number] = False

    def update_column(self, column, number):
        self.possible_numbers[:, column, number] = False

    def update_cell(self, position, number):
        cell_x = (position[0] // self.cell_size) * self.cell_size
        cell_y = (position[1] // self.cell_size) * self.cell_size
        self.possible_numbers[cell_x:cell_x + self.cell_size, cell_y:cell_y + self.cell_size, number] = False

    # def check_positions_single_choice(self):
    #     pass
    #
    # def check_no_options_fields(self):
    #     pass
    #
    # def find_position_single_choice(self):
    #     pass
    #
    # def fill_position(self):
    #     pass
    #
    # def rollback_last_random(self):
    #     pass
    #
    # def single_number_fill(self, number):
    #     for row_number, row in enumerate(self.grid):
    #         choices = np.arange(0, self.total_size)
    #         rules_passed = False
    #         out_of_options = False
    #         while not rules_passed:
    #             generated_position = [row_number, np.random.choice(choices)]
    #             rules_passed = self.check_rules(generated_position, number)
    #             if rules_passed:
    #                 self.grid[tuple(generated_position)] = number
    #             else:
    #                 choices = np.delete(choices, np.where(choices == generated_position[1]))
    #                 out_of_options = not choices.any()
    #         if out_of_options:
    #             break
    #
    # def check_rules(self, position_to_occupy, number):
    #     column_ok = self.check_column(position_to_occupy[1], number)
    #     position_ok = self.check_position(position_to_occupy)
    #     cell_ok = self.check_cell(position_to_occupy, number)
    #     rules_passed = all([column_ok, position_ok, cell_ok])
    #     return rules_passed
    #
    # def check_position(self, position_to_occupy):
    #     position_free = self.grid[tuple(position_to_occupy)] == 0
    #     return position_free
    #
    # def check_column(self, column_index, number):
    #     column = self.grid[:, column_index]
    #     return not (number in column)
    #
    # def check_cell(self, position, number):
    #     cell_x = (position[0] // self.cell_size) * self.cell_size
    #     cell_y = (position[1] // self.cell_size) * self.cell_size
    #     cell = self.grid[cell_x:cell_x + self.cell_size, cell_y:cell_y + self.cell_size]
    #     result = (number in cell)
    #     return not result
#
# x = Sudoku()
# x.generate_grid()
# print(x.grid)
