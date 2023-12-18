import numpy as np


def solution(a, k):
    length = 0
    floor_sum = k
    a = np.array(a)

    while floor_sum >= k:
        length += 1
        floor_sum = np.sum(a // length)
    return length - 1
