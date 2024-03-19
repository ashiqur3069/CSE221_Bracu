def DFS(graph, start):
    visited = {i: False for i in graph}
    stack = [start]
    visited[start] = True
    dfs_path = []

    while stack:
        node = stack.pop()
        dfs_path.append(node)

        for child in reversed(graph[node]):
            if not visited[child]:
                visited[child] = True
                stack.append(child)

    return dfs_path

with open("input3.txt","r") as file:
    N, M = map(int, file.readline().split())
    graph = {i: [] for i in range(1, N + 1)}
    for i in range(M):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    output = DFS(graph, 1)
    with open("output3.txt","w") as file2:
        file2.write(" ".join(map(str, output)))
