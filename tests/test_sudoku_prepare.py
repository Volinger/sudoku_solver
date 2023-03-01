import numpy as np
import pytest
import numpy
import sudoku.sudoku_prepare as sudoku_prepare


@pytest.fixture
def sudoku_preparer():
    return sudoku_prepare.SudokuPreparer(size=4, seed=50)


class TestSudokuPreparer:

    def test_prepare(self, sudoku_preparer):
        expected = [[1, 2, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 2]]
        sudoku_preparer.prepare(15)
        assert (sudoku_preparer.sudoku.grid == expected).all()

    def test_remove_random_number(self, sudoku_preparer):
        assert sudoku_preparer.remove_random_number()
