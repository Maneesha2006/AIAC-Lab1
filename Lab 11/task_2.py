class QueueList:

    def __init__(self):
        self._items = []

    def enqueue(self, item):

    
        self._items.append(item)

    def dequeue(self):
        
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        
        return len(self._items) == 0

# Test QueueList
if __name__ == "__main__":
    print("Testing QueueList (using list):")
    q = QueueList()
    print("Is queue empty?", q.is_empty())  # True
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Is queue empty?", q.is_empty())  # False
    print("Dequeued:", q.dequeue())  # 1
    print("Dequeued:", q.dequeue())  # 2
    print("Dequeued:", q.dequeue())  # 3
    print("Is queue empty?", q.is_empty())  # True

print("\n--- AI Performance Review ---")
# Optimized version using collections.deque
from collections import deque

class QueueDeque:

    def __init__(self):
        
        self._items = deque()

    def enqueue(self, item):
        
        self._items.append(item)

    def dequeue(self):
        
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self):
        
        return len(self._items) == 0

if __name__ == "__main__":
    print("Testing QueueDeque (using deque):")
    qd = QueueDeque()
    print("Is queue empty?", qd.is_empty())  # True
    qd.enqueue(10)
    qd.enqueue(20)
    qd.enqueue(30)
    print("Is queue empty?", qd.is_empty())  # False
    print("Dequeued:", qd.dequeue())  # 10
    print("Dequeued:", qd.dequeue())  # 20
    print("Dequeued:", qd.dequeue())  # 30
    print("Is queue empty?", qd.is_empty())  

