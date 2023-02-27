"""
Tests for sudoku generation algorithm
"""
import pytest
import numpy as np
import sudoku.sudoku as sudoku


@pytest.fixture
def sudoku_fixture():
    return sudoku.Sudoku(size=4)


class TestSudoku:

    def test_get_next_free_position(self, sudoku_fixture):
        sudoku_fixture.grid[0, 0] = 1
        assert sudoku_fixture.get_next_free_position() == (0, 1)

    def test_update_options_single_number(self, sudoku_fixture):
        sudoku_fixture.update_options_single_number((1, 1), 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[0:2, 0:2, 1] = False
        expected[:, 1, 1] = False
        expected[1, :, 1] = False
        assert (sudoku_fixture.possible_numbers == expected).all()

    def test_update_row(self, sudoku_fixture):
        sudoku_fixture.update_row(1, 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[1, :, 1] = False
        assert (sudoku_fixture.possible_numbers == expected).all()

    def test_update_column(self, sudoku_fixture):
        sudoku_fixture.update_column(1, 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[:, 1, 1] = False
        assert (sudoku_fixture.possible_numbers == expected).all()

    def test_update_cell(self, sudoku_fixture):
        sudoku_fixture.update_cell((1, 1), 2)
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[0:2, 0:2, 1] = False
        assert (sudoku_fixture.possible_numbers == expected).all()

    def test_reset_possible_numbers(self, sudoku_fixture):
        sudoku_fixture.grid[1, 1] = 2
        sudoku_fixture.grid[0, 0] = 3
        sudoku_fixture.number_selection_memory = [(0, 0), (1, 1)]
        sudoku_fixture.reset_possible_numbers()
        expected = np.ndarray((4, 4, 4), dtype=bool)
        expected.fill(True)
        expected[0:2, 0:2, 1] = False
        expected[:, 1, 1] = False
        expected[1, :, 1] = False
        expected[0:2, 0:2, 2] = False
        expected[:, 0, 2] = False
        expected[0, :, 2] = False
        assert (sudoku_fixture.possible_numbers == expected).all()