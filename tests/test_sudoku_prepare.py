import pytest
import numpy
import sudoku.sudoku_prepare as sudoku_prepare


@pytest.fixture
def sudoku_preparer():
    return sudoku_prepare.SudokuPreparer()

@pytest.fixture()
def completed_sudoku():
    return [[1, 2, 4, 3]
            [4, 3, 2, 1]
            [2, 1, 3, 4]
            [3, 4, 1, 2]]

class TestSudokuPreparer:

    def test_generate(self, sudoku_preparer):
        assert False

    def test_prepare(self, sudoku_preparer):
        assert False

    def test_remove_numbers(self, sudoku_preparer):
        assert False

    def test_remove_random_number(self, sudoku_preparer):
        assert False

    def test_check_solvable(self, sudoku_preparer):
        assert False