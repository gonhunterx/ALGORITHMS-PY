from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
       self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer) 
    

que = Queue()

orders = ['pizza', 'somosa', 'pasta', 'biryani', 'burger']

for item in orders:
    que.enqueue(item)

print(que.size())
print(f"{que.buffer}")
