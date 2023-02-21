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