lst = [1,54,521,62,66,2,73,12,78]
target = 73
l,r = 0, len(lst) - 1


while l < r:
    m = (l + r) // 2 
    if lst[m] == target:
        print(f"{target} at index: {m}")
        break
    elif lst[m] > target:
        r = m - 1
    elif lst[m] < target:
        l = m + 1

