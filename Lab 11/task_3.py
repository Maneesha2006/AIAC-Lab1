class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 

    def delete_value(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:

                    self.head = current.next  # Pointer update: head now points to next node
                else:
                    # Bypass the current node
                    prev.next = current.next  # Pointer update: previous node skips current
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """Traverse the list and return a list of node values."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next  # Move to the next node
        return elements

# --- Test cases to validate all operations ---

if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()

    # Test 1: Insert at end
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("After insertions:", ll.traverse())  # Expected: [10, 20, 30]

    # Test 2: Delete head node
    ll.delete_value(10)
    print("After deleting head (10):", ll.traverse())  # Expected: [20, 30]

    # Test 3: Delete middle node
    ll.insert_at_end(40)
    ll.delete_value(30)
    print("After deleting middle (30):", ll.traverse())  # Expected: [20, 40]

    # Test 4: Delete last node
    ll.delete_value(40)
    print("After deleting last (40):", ll.traverse())  # Expected: [20]

    # Test 5: Delete non-existent value
    result = ll.delete_value(99)
    print("Attempt to delete non-existent (99):", result, ll.traverse())  # Expected: False, [20]

    # Test 6: Delete only remaining node
    ll.delete_value(20)
    print("After deleting only node (20):", ll.traverse())  # Expected: []

    # Test 7: Insert after all deletions
    ll.insert_at_end(50)
    print("After inserting into empty list:", ll.traverse())  # Expected: [50]
