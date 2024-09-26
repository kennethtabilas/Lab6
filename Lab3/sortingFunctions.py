'''
    File name: python_Lab1.py
    Author: Kenneth Tabilas 
    Date created: 09/23/2024
    Python Version: 3.6.9 
'''

import time, random

# Implementation of insertionSort algorithm
def insertionSort(list_to_sort:list) -> list:
    # Loop through each element in the list starting from index 1
    for i in range(1, len(list_to_sort)):
        # Current element to be sorted
        current_value = list_to_sort[i]
        # Position of the previous element
        j = i - 1
        # Shift elements of the sorted portion of the list that are greater than current_value
        # to one position ahead of their current position
        while j >= 0 and list_to_sort[j] > current_value:
            list_to_sort[j + 1] = list_to_sort[j]
            j -= 1
        # Insert the current_value into the correct position
        list_to_sort[j + 1] = current_value
    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort: list) -> list:
    # Loop through the entire list
    for i in range(len(list_to_sort) - 1):
        # Flag to track if any swaps are made
        swapped = False
        # Perform a pass over the list, ignoring the last i elements which are already sorted
        for j in range(len(list_to_sort) - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                # Swap adjacent elements if they are in the wrong order
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                swapped = True
        # If no swaps were made in this pass, the list is already sorted
        if not swapped:
            break
    return list_to_sort


# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time


if __name__ == '__main__':
    print(f"Insertion sort runtime (100 elements): {getRuntime(insertionSort, 100)} seconds")
    print(f"Bubble sort runtime (100 elements): {getRuntime(bubbleSort, 100)} seconds")
