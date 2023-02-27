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
        assert (sudoku_preparer.prepare(15) == expected).all()

    def test_remove_random_number(self, sudoku_preparer):
        assert sudoku_preparer.remove_random_number()

    def test_check_solvable__true(self, sudoku_preparer):
        sudoku_preparer.generator.sudoku.grid[0, 1] = 0
        assert sudoku_preparer.check_solvable()

    def test_check_solvable__false(self, sudoku_preparer):
        sudoku_preparer.generator.sudoku.grid = np.zeros((4, 4))
        sudoku_preparer.generator.sudoku.possible_numbers.fill(True)
        sudoku_preparer.generator.rollbacked_filter.fill(True)
        sudoku_preparer.generator.number_selection_memory = []
        assert not sudoku_preparer.check_solvable()