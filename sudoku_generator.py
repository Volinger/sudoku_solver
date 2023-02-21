import numpy as np

class Sudoku:

    def __init__(self, size):
        self.total_size = size #size of sudoku = total_size * total_size, can be 2,4,9
        self.grid = np.zeros((self.total_size, self.total_size))
        self.cell_size = int(self.total_size**0.5)
        self.possible_numbers = np.ndarray((self.total_size, self.total_size, self.total_size), dtype=bool)
        self.possible_numbers.fill(True)
        # self.free_positions = np.ndarray((self.total_size, self.total_size), dtype=bool)
        # self.free_positions.fill(True)
        self.number_selection_memory = []
        self.number_selection_random = []
        self.next_position = (0, 0)

    def generate_grid(self):
        np.random.seed(50)
        while any(self.free_positions):
            self.randomly_fill_next_position()
            self.update_available_options()
            self.fill_options_single_choice()

    def randomly_fill_next_position(self):
        available_options = self.grid[self.next_position]
        choice = np.random.choice(available_options)
        self.grid[self.next_position] = choice
        self.free_positions[self.next_position] = False
        self.number_selection_memory.append(self.next_position)
        self.number_selection_random.append(True)

    def fill_options_single_choice(self):
        position_filled = True
        while position_filled:
            self.check_positions_single_choice()
            position_filled = self.fill_positions_single_choice()
            if position_filled:
                self.update_available_options()
                no_options = self.check_no_options_fields()
                if no_options:
                    self.rollback_last_random()

    def update_available_options(self, new_pos, new_number):
        self.grid[new_pos] = new_number
        positions = np.nditer(self.grid, flags=['multi_index'])
        for number in positions:
            self.update_options_single_number(position, number)
            print("%d <%s>" % (number, positions.multi_index), end=' ')

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
        self.grid[cell_x:cell_x + self.cell_size, cell_y:cell_y + self.cell_size, number] = False

    def fill_position_single_choice(self):
        position = self.find_position_single_choice()
        if position == ():
            return False

    def check_positions_single_choice(self):
        pass

    def check_no_options_fields(self):
        pass

    def find_position_single_choice(self):
        pass

    def fill_position(self):
        pass

    def rollback_last_random(self):
        pass

    def single_number_fill(self, number):
        for row_number, row in enumerate(self.grid):
            choices = np.arange(0, self.total_size)
            rules_passed = False
            out_of_options = False
            while not rules_passed:
                generated_position = [row_number, np.random.choice(choices)]
                rules_passed = self.check_rules(generated_position, number)
                if rules_passed:
                    self.grid[tuple(generated_position)] = number
                else:
                    choices = np.delete(choices, np.where(choices == generated_position[1]))
                    out_of_options = not choices.any()
            if out_of_options:
                break

    def check_rules(self, position_to_occupy, number):
        column_ok = self.check_column(position_to_occupy[1], number)
        position_ok = self.check_position(position_to_occupy)
        cell_ok = self.check_cell(position_to_occupy, number)
        rules_passed = all([column_ok, position_ok, cell_ok])
        return rules_passed

    def check_position(self, position_to_occupy):
        position_free = self.grid[tuple(position_to_occupy)] == 0
        return position_free

    def check_column(self, column_index, number):
        column = self.grid[:, column_index]
        return not (number in column)

    def check_cell(self, position, number):
        cell_x = (position[0] // self.cell_size) * self.cell_size
        cell_y = (position[1] // self.cell_size) * self.cell_size
        cell = self.grid[cell_x:cell_x + self.cell_size, cell_y:cell_y + self.cell_size]
        result = (number in cell)
        return not result

x = Sudoku()
x.generate_grid()
print(x.grid)
