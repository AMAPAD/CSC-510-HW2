"""
merge_sort.py

This module implements the Merge Sort algorithm, a divide-and-conquer sorting algorithm.
It splits the input array into smaller sub-arrays, recursively sorts them, and then
merges the sorted sub-arrays to produce the final sorted array.

Functions:
    mergeSort(arr): Recursively splits an array into halves and merges the sorted halves.
    recombine(left_arr, right_arr): Merges two sorted arrays into one sorted array.
    
Example usage:
    arr = rand.random_array([None] * 20)
    sorted_arr = mergeSort(arr)
    print(sorted_arr)
"""

import rand


def merge_sort(arr):
    """
    Recursively sorts an array using the Merge Sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: A new array containing the sorted elements of the input array.
    """

    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left_arr (list): The left half of the array, already sorted.
        right_arr (list): The right half of the array, already sorted.

    Returns:
        list: A new array that contains all elements of left_arr and right_arr, sorted.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1
        
    return merge_arr


arr_in = rand.random_array([None] * 20)
arr_out = merge_sort(arr_in)

print(arr_out)