def topological_sort(V, edges):
    graph = {i: [] for i in range(V)}
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * V
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for i in range(V):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]

V = 6
E = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]
result = topological_sort(V, E)
print(result)
