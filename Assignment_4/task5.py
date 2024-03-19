def shortest_path(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        node, path = queue.pop(0)
        visited.add(node)

        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None

graph = {}
with open("input5.txt", "r") as file:
    N, M, D = map(int, file.readline().split())
    for i in range(1, N + 1):
        graph[i] = []
    for i in range(M):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)
shortest_path = shortest_path(graph, 1, D)
time_taken = len(shortest_path) - 1
with open("output5.txt", "w") as file:
    file.write(f"Time: {str(time_taken)}\n")
    file.write(f"Shortest Path: {' '.join(map(str, shortest_path))}\n")