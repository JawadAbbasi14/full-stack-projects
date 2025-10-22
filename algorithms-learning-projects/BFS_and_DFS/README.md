

# 🌐 Graph Search Algorithms: BFS and DFS

Ye Python script ek **undirected graph** ke liye **Breadth-First Search (BFS)** aur **Depth-First Search (DFS)** algorithms implement karti hai. Saath hi, graph ko visually represent karne ke liye `matplotlib` aur `networkx` ka use kiya gaya hai.

## 📌 Features

- Graph representation using **adjacency list**
- **BFS** traversal using queue
- **DFS** traversal using recursion
- **Graph visualization** with customizable layout and colors

## 🧠 Algorithms Explained

### 🔍 Breadth-First Search (BFS)
- BFS graph ke nodes ko level-wise explore karta hai.
- Queue ka use hota hai taake pehle aaye nodes pehle process ho.
- Har node ke neighbors ko visit karte hain agar wo pehle visit nahi hue.

### 🧗 Depth-First Search (DFS)
- DFS graph ko depth mein explore karta hai.
- Recursion ka use hota hai taake har branch ko pura traverse kare.
- Har node ke unvisited neighbors pe recursive call hoti hai.

## 🧪 Example Usage

```python
if __name__ == "__main__":
    g = Graph()

    # Graph ke edges define karo
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    # Traversals run karo
    print("BFS Traversal starting from node 0:", g.bfs(0))
    print("DFS Traversal starting from node 0:", g.dfs(0))

    # Graph visualize karo
    g.visualize()
```

## 📊 Visualization

Graph ko visually represent karne ke liye `networkx` ka `spring_layout` use hota hai. Nodes aur edges ko color aur size ke saath customize kiya gaya hai taake output visually appealing ho.

## 🛠 Requirements

Install required libraries before running:

```bash
pip install matplotlib networkx
```

## 📁 File Structure

- `Graph` class: Graph creation and traversal logic
- `add_edge(u, v)`: Adds undirected edge between nodes `u` and `v`
- `bfs(start)`: Returns BFS traversal from `start` node
- `dfs(start)`: Returns DFS traversal from `start` node
- `visualize()`: Displays the graph using matplotlib

## 🎯 Use Cases

- Graph theory learning and visualization
- Algorithm teaching tools
- Interview preparation for BFS/DFS
- Educational demos and projects



