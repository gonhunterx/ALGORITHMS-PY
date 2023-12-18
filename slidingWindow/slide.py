arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3

max_val = 0
current_sum = 0


def max_sum(arr, k):
    global max_val
    global current_sum
    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_val = max(max_val, current_sum)
            # subtracting the first element of the window to
            # maintain the window size
            current_sum -= arr[i - (k - 1)]
    return max_val


max_sum(arr, k)
print(max_val)
