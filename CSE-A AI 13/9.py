from collections import deque

# BFS Implementation for TSP
def bfs_tsp(graph, start_node):
    num_nodes = len(graph)
    queue = deque([(start_node, [start_node])])  # Queue holds (current_node, path)
    
    while queue:
        node, path = queue.popleft()
        
        # If all nodes are visited, complete the tour by returning to start_node
        if len(path) == num_nodes:
            return path + [start_node]
        
        for neighbour in graph[node]:
            if neighbour not in path:  # Check if the neighbor is already visited in the current path
                queue.append((neighbour, path + [neighbour]))
    
    return None  # If no tour is found

# DFS Implementation for TSP
def dfs_tsp(graph, start_node):
    num_nodes = len(graph)

    def dfs(current_node, path):
        if len(path) == num_nodes:
            return path + [start_node]  # Complete the tour
        
        for neighbour in graph[current_node]:
            if neighbour not in path:  # Ensure the node is not revisited in the current path
                tour = dfs(neighbour, path + [neighbour])
                if tour:
                    return tour
        
        return None

    return dfs(start_node, [start_node])

# Example graph for demonstration
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
start_node = 0

# Run BFS and DFS TSP functions
print("BFS:", bfs_tsp(graph, start_node))
print("DFS:", dfs_tsp(graph, start_node))
