from collections import deque

# Graph ko dictionary ke zariye represent karna
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# --- Breadth-First Search (BFS) ---
def bfs(graph, start_node):
    """
    Graph par BFS traversal karta hai.
    """
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    print("BFS Traversal Order:")
    
    while queue:
        # Queue ke left se node nikalna (FIFO)
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Padosi nodes ko explore karna
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print("\n")

# --- Depth-First Search (DFS) (Iterative) ---
def dfs_iterative(graph, start_node):
    """
    Graph par iterative DFS traversal karta hai.
    """
    visited = set()
    stack = [start_node]
    
    print("DFS Traversal (Iterative):")
    
    while stack:
        # Stack ke top se node nikalna (LIFO)
        current_node = stack.pop()
        
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
            
            # Padosi nodes ko stack mein dalna
            # Reverse order mein, taake output consistent ho
            for neighbor in reversed(graph.get(current_node, [])):
                stack.append(neighbor)
    print("\n")

# --- Depth-First Search (DFS) (Recursive) ---
def dfs_recursive_helper(graph, node, visited):
    """
    Recursive DFS ke liye helper function.
    """
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs_recursive_helper(graph, neighbor, visited)

def dfs_recursive(graph, start_node):
    """
    Graph par recursive DFS traversal karta hai.
    """
    visited = set()
    print("DFS Traversal (Recursive):")
    dfs_recursive_helper(graph, start_node, visited)
    print("\n")


# --- Example Usage ---
if __name__ == "__main__":
    
    # BFS ko run karna
    bfs(graph, 'A')
    
    # Iterative DFS ko run karna
    dfs_iterative(graph, 'A')
    
    # Recursive DFS ko run karna
    dfs_recursive(graph, 'A')
