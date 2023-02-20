import numpy as np

class Sudoku:
    # select 1's
    # for each row, select by random position
    # if not possible, try next position
    # if no position is available, return to previous generation step
    # repeat for all numbers until all positions filled
    def __init__(self):
        self.total_size = 4 #size of sudoku = total_size * total_size, can be 2,4,9
        self.grid = np.zeros((self.total_size, self.total_size))

    def generate_grid(self):
        np.random.seed(50)
        for number in range(1, self.total_size+1):
            self.single_number_fill(number)

    def single_number_fill(self, number):
        for row_number, row in enumerate(self.grid):
            generated_position = [row_number, np.random.randint(1, self.total_size)]
            rules_passed = False
            out_of_options = False
            while not (rules_passed or out_of_options):
                rules_passed = self.check_rules(generated_position, number)
                if rules_passed:
                    self.grid[tuple(generated_position)] = number
                else:
                    if generated_position[1] <= (-self.total_size):
                        out_of_options = True
                    generated_position[1] -= 1
            if out_of_options:
                raise ArithmeticError

    def check_rules(self, position_to_occupy, number):
        column_ok = self.check_column(position_to_occupy[1], number)
        position_ok = self.check_position(position_to_occupy)
        rules_passed = all([column_ok, position_ok])
        return rules_passed

    def check_position(self, position_to_occupy):
        position_free = self.grid[tuple(position_to_occupy)] == 0
        return position_free

    def check_column(self, column_index, number):
        column = self.grid[:, column_index]
        return not np.isin(number, column)

    def check_cell(self, cell, number):
        pass

x = Sudoku()
x.generate_grid()
print(x.grid)
