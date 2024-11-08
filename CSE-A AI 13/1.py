graph={
    'a':['b','c','d'],
    'b':['d'],
    'c':[],
    'd':['e'],
    'e':[]
}
visited=set()
def dfs(graph,visited,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,visited,neighbour)
print("Following is dfs:")
dfs(graph,visited,'a')