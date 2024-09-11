import pytest
from debugging import merge_sort

def test_merge_sort_basic():
    input_arr = [12, 4, 6, 7, 2]
    expected_output = [2, 4, 6, 7, 12]
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_empty():
    input_arr = []
    expected_output = []
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_negative():
    input_arr = [12, 4, -6, 7, -2]
    expected_output = [-6, -2, 4, 7, 12]
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_invalid_input():
    input_arr = [1, 'string', 3.5, 4]
    with pytest.raises(ValueError):
        merge_sort(input_arr)