def BFS(graph, start):
    visited = {i: False for i in graph}
    queue = [start]
    visited[start] = True
    bfs_path = []

    while queue:
        node = queue.pop(0)
        bfs_path.append(node)

        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)

    return bfs_path

with open("input2.txt","r") as file:
    N, M = map(int, file.readline().split())
    graph = {i: [] for i in range(1, N + 1)}
    for i in range(M):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    output = BFS(graph,1)
    with open("output2.txt","w") as file2:
        file2.write(" ".join(map(str, output)))
