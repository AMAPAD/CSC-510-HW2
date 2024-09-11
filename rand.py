"""
random_array_generator.py

This module generates a random array using the `shuf` command through a subprocess call.
It populates an input list with random numbers in a specified range.

Functions:
    random_array(arr): Populates a given list with random integers between 1 and 20.
"""
import subprocess


def random_array(arr):
    """
    Populates the input array with random integers between 1 and 20.
    
    For each index of the array, a random number is generated using the 'shuf' command, and 
    the result is converted to an integer and placed in the array.

    Args:
        arr (list): A list that will be populated with random integers.
    
    Returns:
        list: The input list with randomly generated integers between 1 and 20.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
        
    return arr
