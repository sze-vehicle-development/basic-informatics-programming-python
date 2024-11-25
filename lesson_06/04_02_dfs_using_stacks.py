# Define a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Visit all the nodes of a graph using DFS
# Iterative implementation of DFS using FIFO queue

def dfs(graph, start):
    visited = set()
    stack = []
    stack.append(start)
    visited.add(start)
    while stack:
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
    return visited

# Driver Code
visited = dfs(graph, 'A')
# Output
print(visited)