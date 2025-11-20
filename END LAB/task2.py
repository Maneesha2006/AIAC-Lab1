class Queue:
    """
    A simple Queue implementation for hospital patient management.
    Provides enqueue, dequeue, and peek operations.

    Attributes:
        items (list): Internal list to store queue elements.
    """
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """
        Add a patient to the end of the queue.
        
        Args:
            item: Patient to add to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the patient at the front of the queue.
        
        Returns:
            The patient at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue.")
        return self.items.pop(0)

    def peek(self):
        """
        Return the patient at the front of the queue without removing them.
        
        Returns:
            The patient at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue.")
        return self.items[0]

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def __len__(self):
        """
        Return the number of patients in the queue.

        Returns:
            int: Number of patients in the queue.
        """
        return len(self.items)

    def __repr__(self):
        """Return a string representation of the queue."""
        return f"Queue({self.items})"


# --------------------
# Unit tests for Queue
# --------------------
def test_queue():
    print("Testing Queue implementation...")

    q = Queue()

    # Queue should be empty initially
    assert q.is_empty() is True
    assert len(q) == 0

    # Enqueue patients
    q.enqueue("Patient A")
    q.enqueue("Patient B")
    q.enqueue("Patient C")

    assert not q.is_empty()
    assert len(q) == 3

    # Peek should return "Patient A"
    assert q.peek() == "Patient A"

    # Dequeue should return "Patient A"
    assert q.dequeue() == "Patient A"
    assert len(q) == 2

    # Peek should now return "Patient B"
    assert q.peek() == "Patient B"

    # Dequeue remaining patients
    assert q.dequeue() == "Patient B"
    assert q.dequeue() == "Patient C"
    assert q.is_empty() is True

   
    try:
        q.dequeue()
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError when dequeue from empty queue"

    try:
        q.peek()
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError when peek from empty queue"

    print("All Queue tests passed.")


if __name__ == "__main__":
    test_queue()

