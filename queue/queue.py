stock_price_queue = []

stock_price_queue.insert(0,131.10)
stock_price_queue.insert(0,132.12)
stock_price_queue.insert(0,135)

print(stock_price_queue)

# first in first out datastructure 
stock_price_queue.pop()
# 131.1
stock_price_queue.pop()
# 132.12

from collections import deque 
# deque can be used as a stack and a queue 
q = deque()
q.appendleft(5)
q.appendleft(89)
q.appendleft(123)

q.pop()
# would return 5
# think of a queue like a list to buy a ticket.
# whoever got in line first get their ticket first
# queues always append to the Left or (head in a linked list) of the list.

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

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.buffer)

first_item = pq.dequeue()
print(first_item)