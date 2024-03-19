def DFS(graph, source, visited, parent, stack):
    visited[source] = True
    stack.append(source)

    for adj in graph[source]:
        if not visited[adj]:
            parent[adj] = source
            if DFS(graph, adj, visited, parent, stack):
                return True
        elif parent[adj] != source and adj in stack:
            return True

    stack.remove(source)
    return False

def cyclic(graph):
    visited = {node: False for node in graph}
    print(visited)
    parent = {node: None for node in graph}
    stack = []

    for node in graph:
        if not visited[node]:
            if DFS(graph, node, visited, parent, stack):
                return True

    return False

graph = {}
with open("input4.txt", "r") as file:
    N, M = map(int, file.readline().split())
    for i in range(1, N + 1):
        graph[i] = []
    for j in range(M):
        u, v = map(int, file.readline().split())
        graph[u].append(v)

cycle = cyclic(graph)

with open("output4.txt", "w") as file:
    if cycle:
        file.write("YES")
    else:
        file.write("NO")
