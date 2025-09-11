class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}

    def add_edge(self, u, v):
        # Add an edge from u to v (undirected by default)
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):

        from collections import deque  # Import here to avoid top-level import

        visited = set()  # Track visited nodes
        queue = deque([start])  # Initialize queue with the start node
        order = []  # List to store traversal order

        while queue:
            node = queue.popleft()  # Dequeue the next node
            if node not in visited:
                # Visit the node
                visited.add(node)
                order.append(node)
                # Enqueue all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    def dfs_iterative(self, start):
        """
        Depth-First Search (DFS) traversal (iterative version) from the start node.
        Returns a list of nodes in the order they are visited.
        """
        visited = set()
        stack = [start]  # Use a stack for DFS
        order = []

        while stack:
            node = stack.pop()  # Pop the last node added
            if node not in visited:
                # Visit the node
                visited.add(node)
                order.append(node)
                # Add all unvisited neighbors to the stack
                # Reverse to maintain order similar to recursive DFS
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def dfs_recursive(self, start):
        """
        Depth-First Search (DFS) traversal (recursive version) from the start node.
        Returns a list of nodes in the order they are visited.
        """
        order = []
        visited = set()

        def dfs(node):
            if node not in visited:
                # Visit the node
                visited.add(node)
                order.append(node)
                # Recursively visit all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    dfs(neighbor)

        dfs(start)
        return order

# --- Test cases to demonstrate BFS and DFS traversals ---
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (2, 6)
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("Adjacency List:", g.adj_list)
    print("BFS traversal from node 0:", g.bfs(0))
    print("DFS iterative traversal from node 0:", g.dfs_iterative(0))
    print("DFS recursive traversal from node 0:", g.dfs_recursive(0))

    # Compare DFS iterative vs recursive
    print("DFS iterative == DFS recursive?", g.dfs_iterative(0) == g.dfs_recursive(0))
