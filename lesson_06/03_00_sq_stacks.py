stack = []  # Create an empty stack
stack.append(10)  # Push 10
stack.append(20)  # Push 20
x = stack.pop()  # Pop top element
print(x)

from collections import deque
stack = deque()
stack.append(10)  # Push
stack.append(20)  # Push
x = stack.pop()  # Pop
print(x)
