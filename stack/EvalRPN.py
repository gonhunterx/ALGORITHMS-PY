# with the Reverse polish notation there will always be two
# numbers to append to the stack because the opperands come after
# therefore you could never have tokens = e.g. [1, /]


# RPN is a notation where the operators follow their opperands.
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                # because we are popping the last val in the stack
                # we need to switch the values for the calculation
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(b / a)
            else:
                # using int will round it down to 0 in python
                stack.append(int(char))
        # you have to get the specific value here to make sure return
        # is an int and not a list
        return stack[0]
