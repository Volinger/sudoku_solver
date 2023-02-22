"""
Tests for sudoku generation algorithm
"""
import pytest
import numpy as np
import sudoku_generator.sudoku_generator as sudoku_generator


@pytest.fixture
def sudoku():
    return sudoku_generator.Sudoku(size=4)


class TestSudoku:

    def test_check_no_options__false(self, sudoku):
        assert not sudoku.check_no_options()

    def test_check_no_options__true(self, sudoku):
        sudoku.possible_numbers[2, 2, :] = False
        assert sudoku.check_no_options()

    # def test_generate_grid(self, sudoku):
    #     sudoku.generate_grid()
    #     assert False

    def test_rollback_last_random(self, sudoku):
        sudoku.number_selection_memory = [(1, 1), (2, 2), (3, 3)]
        sudoku.number_selection_random = [True, True, False]
        sudoku.rollback_last_random()
        assert sudoku.number_selection_memory == [(1, 1)] and sudoku.number_selection_random == [True]

    def test_fill_single_choice(self, sudoku):
        sudoku.possible_numbers[3, 3, :3] = False
        sudoku.fill_single_choice((3, 3))
        assert sudoku.grid[3, 3] == 4

    def test_check_next_single_option_position__exists(self, sudoku):
        sudoku.possible_numbers[3, 3, 1:] = False
        assert sudoku.check_next_single_option_position() == (3, 3)

    def test_check_next_single_option_position__none(self, sudoku):
        assert sudoku.check_next_single_option_position() == -1

    def test_reset_available_options(self, sudoku):
        sudoku.grid[1, 1] = 2
        sudoku.grid[0, 0] = int(3)
        sudoku.number_selection_memory = [(0, 0), (1, 1)]
        sudoku.reset_available_options()
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[0:2, 0:2, 2] = False
        expected[:, 1, 2] = False
        expected[1, :, 2] = False
        expected[0:2, 0:2, 3] = False
        expected[:, 0, 3] = False
        expected[0, :, 3] = False
        assert (sudoku.possible_numbers == expected).all()

    def test_update_options_single_number(self, sudoku):
        sudoku.update_options_single_number((1, 1), 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[0:2, 0:2, 2] = False
        expected[:, 1, 2] = False
        expected[1, :, 2] = False
        assert (sudoku.possible_numbers == expected).all()

    def test_update_row(self, sudoku):
        sudoku.update_row(1, 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[1, :, 2] = False
        assert (sudoku.possible_numbers == expected).all()

    def test_update_column(self, sudoku):
        sudoku.update_column(1, 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[:, 1, 2] = False
        assert (sudoku.possible_numbers == expected).all()

    def test_update_cell(self, sudoku):
        sudoku.update_cell((1, 1), 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[0:2, 0:2, 2] = False
        assert (sudoku.possible_numbers == expected).all()
