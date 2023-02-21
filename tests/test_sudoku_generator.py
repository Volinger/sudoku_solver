"""
Tests for sudoku generation algorithm
"""
import pytest
import numpy as np
import sudoku_generator


@pytest.fixture
def sudoku_fixture():
    return sudoku_generator.Sudoku(size=4)


class TestSudoku:
    def test_update_row(self):
        sudoku_test = sudoku_fixture()
        sudoku_test.update_row(1, 2)
        expected = np.array((4,4,4))
        expected.fill(True)
        expected[1, :, 2] = False
        assert sudoku_test.grid == expected

    def test_update_column(self):
        sudoku_test = sudoku_fixture()
        sudoku_test.update_column(1, 2)
        expected = np.array((4,4,4))
        expected.fill(True)
        expected[:, 1, 2] = False
        assert sudoku_test.grid == expected

    def test_update_cell(self):
        sudoku_test = sudoku_fixture()
        sudoku_test.update_cell((1,1), 2)
        expected = np.array((4,4,4))
        expected.fill(True)
        expected[0:2, 0:2, 2] = False
        assert sudoku_test.grid == expected