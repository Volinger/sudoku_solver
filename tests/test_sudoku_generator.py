"""
Tests for sudoku generation algorithm
"""
import pytest
import numpy as np
import sudoku.sudoku_generator as sudoku_generator


@pytest.fixture
def generator():
    return sudoku_generator.SudokuGenerator(size=4)


class TestSudokuGenerator:

    def test_get_allowed_numbers(self, generator):
        generator.sudoku.possible_numbers[0, 0, 0] = False
        generator.rollbacked_filter[1, 1, 1] = False
        expected = np.ndarray((generator.sudoku.get_size(), generator.sudoku.get_size(), generator.sudoku.get_size()),
                              dtype=bool)
        expected.fill(True)
        expected[0, 0, 0] = expected[1, 1, 1] = False
        assert (generator.get_allowed_numbers() == expected).all()

    def test_check_no_options__false(self, generator):
        assert not generator.check_no_options()

    def test_check_no_options__true(self, generator):
        generator.sudoku.possible_numbers[2, 2, :] = False
        assert generator.check_no_options()

    def test_generate_grid(self, generator):
        generator.generate_grid(seed=50)
        expected = np.asarray([[1, 2, 4, 3],
                               [4, 3, 2, 1],
                               [2, 1, 3, 4],
                               [3, 4, 1, 2]])
        assert (generator.sudoku.grid == expected).all()

    def test_randomly_fill_next_position(self, generator):
        np.random.seed(50)
        generator.randomly_fill_next_position()
        assert generator.sudoku.grid[0, 0] == 1

    def test_rollback_last_random(self, generator):
        generator.number_selection_memory = [(1, 1), (2, 2), (3, 3)]
        generator.number_selection_random = [True, True, False]
        generator.rollback_last_random()
        assert generator.number_selection_memory == [(1, 1)] and generator.number_selection_random == [True]

    def test_reset_dependent_rollbacks(self, generator):
        generator.generate_grid(seed=50)
        np.put(generator.rollbacked_filter, [(1, 3), (2, 0), (2, 1)], [False, False, False, False])
        expected = generator.rollbacked_filter.copy()
        generator.reset_dependent_rollbacks((2, 0))
        expected[2, 1] = [True, True, True, True]
        assert (generator.rollbacked_filter == expected).all()

    def test_fill_single_choice(self, generator):
        generator.sudoku.possible_numbers[3, 3, :3] = False
        generator.fill_single_choice((3, 3))
        assert generator.sudoku.grid[3, 3] == 4

    def test_check_next_single_option_position__exists(self, generator):
        generator.sudoku.possible_numbers[3, 3, 1:] = False
        assert generator.check_next_single_option_position() == (3, 3)

    def test_check_next_single_option_position__none(self, generator):
        assert generator.check_next_single_option_position() is None
