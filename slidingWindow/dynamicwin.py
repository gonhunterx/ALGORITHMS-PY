arr = [4, 2, 2, 7, 8, 1, 2, 8, 1, 0]
tareget = 8


def smallest_subarray(arr, target):
    window_start = 0
    window_end = len(arr) - 1
    min_window_size = len(arr) + 1
    current_sum = 0
    while ()