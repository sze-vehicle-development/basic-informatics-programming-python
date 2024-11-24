from collections import deque
queue = deque()  # Create an empty queue
queue.append(10)  # Enqueue 10
queue.append(20)  # Enqueue 20
x = queue.popleft()  # Dequeue front element
print(x)
