
from queue import Queue
from queue import LifoQueue

q = Queue()
q.put(10)  # Enqueue
q.put(20)  # Enqueue
x = q.get()  # Dequeue
print(x)

stack = LifoQueue()
stack.put(10)  # Push
stack.put(20)  # Push
x = stack.get()  # Pop
print(x)