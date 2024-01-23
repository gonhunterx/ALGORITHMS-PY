from collections import deque 

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer)==0
    
    def display_queue(self):
        print(self.buffer)
        
    def enqueue_dict(self, key, value):
        self.buffer.appendleft({key:value})
    
def main():
    running = True 
    queue = Queue()
    
    while running: 
        print("""
1. View queue
2. Add to queue
3. Dequeue
4. View queue size
5. Exit
              """)
        choice = input("Input: ")
        if choice == "1":
            queue.display_queue()
        elif choice == "2":
            print("Do you want to enter a single value\nor enter a key: value pair? (1/2)")
            x = input("Input: ")
            if x == "1":
                print("What do you want to add to queue?: ")
                y = input("Input: ")
                queue.enqueue(y)
            elif x == "2":
                key = input("Input a key: ")
                value = input("Input value: ")
                queue.enqueue_dict(key, value)
        elif choice == "5":
            running = False
if __name__ == "__main__":
    main()