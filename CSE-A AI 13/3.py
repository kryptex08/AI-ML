from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    result=[]
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return result

graph={
    'a':['b','c','e'],
    'b':['c'],
    'c':['a','b'],
    'd':['a'],
    'e':['c','d']
}
result=bfs(graph,'a')
print(result)