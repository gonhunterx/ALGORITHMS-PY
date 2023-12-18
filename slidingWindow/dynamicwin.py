arr = [4, 2, 2, 7, 8, 1, 2, 8, 1, 0]
target = 8


def smallest_subarray(arr, target):
    min_window_size = len(arr) + 1
    window_end = len(arr) - 1
    window_start = 0
    current_win_sum = 0
    current_win_sum += min_window_size
    while current_win_sum >= target:
        min_window_size = min(min_window_size, window_end - window_start + 1)
        current_win_sum -= arr[window_start]
        window_start += 1
    return min_window_size


print(smallest_subarray(arr, target))
