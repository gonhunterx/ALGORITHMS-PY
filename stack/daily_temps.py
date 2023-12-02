temperatures = [73, 28, 29, 55, 49]

# VERSION WITH range len


def dailyTemperatures(self, temperatures):
    res = [0] * len(temperatures)
    stack = []  # contain a pair of values [temp, index]

    for i, t in enumerate(temperatures):
        # checking if both the stack and temp value are greater than the
        # last value in the stack
        # [-1] is giving us the last item (top of stack) and [0]
        # is the value of that item at that index
        while stack and t > stack[-1][0]:
            # stack temp and stack index popped
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append([i, t])
    return res


stack = []
result = [0] * len(temperatures)

for i in range(len(temperatures)):
    while stack and i > temperatures[stack[-1]]:
        # pop the top item in the stack
        prev_index = stack.pop()
        result[prev_index] = i - prev_index

    stack.append(i)
# return result
