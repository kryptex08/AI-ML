import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bestfs(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    visited = set()
    visited.add(start)
    path = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:
        current_priority, current_node = heapq.heappop(open_list)
        path.append(current_node)

        if current_node == goal:
            return path

        for direction in directions:
            neighbour = (current_node[0] + direction[0], current_node[1] + direction[1])

            if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[0]):
                if grid[neighbour[0]][neighbour[1]] != 1 and neighbour not in visited:
                    visited.add(neighbour)
                    priority = heuristic(neighbour, goal)
                    heapq.heappush(open_list, (priority, neighbour))

    return None 
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (3, 4)
path = bestfs(grid, start, goal)
print("Path =", path)
