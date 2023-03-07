import numpy as np
import pytest
import sudoku.sudoku_prepare as sudoku_prepare
import sudoku.sudoku_generator as sudoku_generator


@pytest.fixture
def sudoku_preparer():
    generator = sudoku_generator.SudokuGenerator(size=4)
    generator.generate_grid()
    prepared = sudoku_prepare.SudokuPreparer(sudoku=generator.sudoku)
    return prepared


class TestSudokuPreparer:

    def test_prepare(self, sudoku_preparer):
        expected = [[1, 2, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 2]]
        sudoku_preparer.prepare(15)
        assert (sudoku_preparer.sudoku.grid == expected).all()

    def test_remove_random_number(self,  sudoku_preparer):
        assert sudoku_preparer.remove_random_number()
