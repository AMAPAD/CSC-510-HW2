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

def test_merge_sort_invalid():
    input_arr = [1, 'string', 3.5, 4]
    with pytest.raises(ValueError):
        merge_sort(input_arr)

def test_merge_sort_floats():
    input_arr = [12.5, 4, 6.7, 7.3, 2]
    expected_output = [2, 4, 6.7, 7.3, 12.5]
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_duplicates():
    input_arr = [5, 1, 7, 7, 2, 1]
    expected_output = [1, 1, 2, 5, 7, 7]
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_sorted():
    input_arr = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_single():
    input_arr = [7]
    expected_output = [7]
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_large():
    input_arr = list(range(1000, 0, -1))
    expected_output = list(range(1, 1001))
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_mixed():
    input_arr = [0, -1, 5, -3, 4, 0]
    expected_output = [-3, -1, 0, 0, 4, 5]
    assert merge_sort(input_arr) == expected_output
