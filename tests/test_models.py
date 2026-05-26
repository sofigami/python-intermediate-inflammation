"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max
from inflammation.models import daily_min

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_real_numbers():
    """Test that max function works for an array of real numbers."""

    test_input = np.array([[1, -2, 6],
                           [3.17, 4, 5.2],
                           [5, 6.0, 4]])
    test_result = np.array([5, 6, 6])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min_real_numbers():
    """Test that min function works for an array of real numbers."""

    test_input = np.array([[1, -2, 6],
                           [3.17, 4, 5.2],
                           [5, 6.0, 4]])
    test_result = np.array([1, -2, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_max_string():
    """ Test for TypeError when parsing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_max(['Hello', 'there'])

def test_daily_max_empty_array():
    """Test that daily_max raises ValueError when given an empty array."""
    with pytest.raises(ValueError):
        daily_max([])

def test_daily_max_nan_propagation():
    data = np.array([[1, np.nan], [3, 4]])
    result = daily_max(data)
    assert np.isnan(result[1])  # documents current behavior

def test_daily_mean_string():
    """ Test for TypeError when parsing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_mean(['Hello', 'there'])

def test_daily_mean_noniterable():
    """ Test mean for IndexError when parsing noniterable argument """

    with pytest.raises(IndexError):
        error_expected = daily_mean(3)      

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0, 0], [0, 0], [0, 0]], [0, 0]),
            ([[1, 2], [3, 4], [5, 6]], [3, 4]),
            (np.zeros((3, 5)), np.zeros((5)))
        ]
)

def test_daily_mean(test_input, test_result):
    """ Test that mean function works for both zeros and integers"""

    npt.assert_array_equal(daily_mean(test_input), test_result)

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[0, 0], [0, 0], [0, 0]], [0, 0]),
            ([[1, 2], [3, 4], [5, 6]], [5, 6]),
            (np.zeros((3, 5)), np.zeros((5))),
            ([[0], [0], [0]], [0]),
            ([[0, 0, 0]], [0, 0, 0]),
            ([[0]], [0]),
            ([0], 0),
            (0, 0)
        ]
)

def test_daily_max(test_input, test_result):
    """ Test that max function works for both zeros and integers"""

    npt.assert_array_equal(daily_max(test_input), test_result)

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
            ([ [1, 2, -1],[3, -2, 4],[5, -9, 6]], [1,-9,-1]),
            ([[0, 1, 2], [0, 3, 4]], [0, 1, 2]),     # array containing zeros
            ([[3, 3, 3], [3, 3, 3], [3, 3, 3]], [3, 3, 3]), # all values the same
        ])
def test_daily_min(test_input, test_result):
    """Test that min function works for an array of positive and negative integers."""
    npt.assert_array_equal(daily_min(test_input), test_result)