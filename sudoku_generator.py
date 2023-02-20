import numpy as np

class Sudoku:
    # select 1's
    # for each row, select by random position
    # if not possible, try next position
    # if no position is available, return to previous generation step
    # repeat for all numbers until all positions filled
    def __init__(self):
        self.total_size = 9 #size of sudoku = total_size * total_size, can be 2,4,9
        self.grid = np.zeros((self.total_size, self.total_size))
        self.cell_size = int(self.total_size**0.5)
        self.possible_numbers = [[list(range(self.total_size))]*self.total_size]*self.total_size
        self.number_selection_memory = []

    def generate_grid(self):
        np.random.seed(50)
        for number in range(1, self.total_size+1):
            self.single_number_fill(number)

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
