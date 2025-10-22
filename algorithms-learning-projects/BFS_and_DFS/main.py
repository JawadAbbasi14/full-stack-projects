# Graph Search Algorithms: BFS and DFS
# Yeh code ek undirected graph ke liye BFS aur DFS implement karta hai.
# Graph adjacency list ke form mein hai.

from collections import defaultdict, deque
import matplotlib.pyplot as plt
import networkx as nx

# Graph class banate hain jo adjacency list use karta hai
class Graph:
    def __init__(self):
        # Defaultdict se har node ke liye empty list ban jaati hai
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        # Undirected graph ke liye dono direction mein edge add karte hain
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
        # BFS implementation
        visited = set()  # Track karega konsa node visit hua
        queue = deque([start])  # Queue mein start node daal do
        visited.add(start)  # Start node ko visited mark karo
        traversal = []  # Yeh store karega traversal order
        
        while queue:
            node = queue.popleft()  # Queue se pehla node nikalo
            traversal.append(node)  # Traversal list mein add karo
            
            # Saare neighbors check karo
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Unvisited neighbor ko queue mein daalo
                    visited.add(neighbor)  # Usay visited mark karo
        
        return traversal
    
    def dfs(self, start):
        # DFS implementation
        visited = set()  # Track karega konsa node visit hua
        traversal = []  # Yeh store karega traversal order
        
        def dfs_recursive(node):
            # Recursive DFS function
            visited.add(node)  # Node ko visited mark karo
            traversal.append(node)  # Traversal list mein add karo
            
            # Saare neighbors check karo
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)  # Unvisited neighbor ke liye recursive call
        
        dfs_recursive(start)  # DFS shuru karo
        return traversal
    
    def visualize(self):
        # Graph ko visualize karne ke liye networkx use karenge
        G = nx.Graph()
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)
        
        pos = nx.spring_layout(G)  # Layout for visualization
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='#5b67f3', 
                node_size=500, font_color='#333333', edge_color='#ff6b6b')
        plt.title("Graph Visualization (BFS/DFS)")
        plt.show()

# Example usage
if __name__ == "__main__":
    g = Graph()
    
    # Graph mein edges add karo
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    
    # BFS aur DFS run karo
    print("BFS Traversal starting from node 0:", g.bfs(0))
    print("DFS Traversal starting from node 0:", g.dfs(0))
    
    # Graph ko visualize karo
    g.visualize()
