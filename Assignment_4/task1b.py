def adj_list(N, M, edges):
    adjacency_list = {i: [] for i in range(N + 1)}
    for i in edges:
        row, col, val = i
        adjacency_list[row].append((col, val))
    return adjacency_list

with open("input1b.txt","r") as file:
    N, M = map(int, file.readline().split())
    edges = []
    for i in range(M):
        row, col, val = map(int, file.readline().split())
        edges.append((row, col, val))
    adjacency_list = adj_list(N, M, edges)
    print(edges)
    with open("output1b.txt","w") as file2:
        for i, j in adjacency_list.items():
            file2.write(str(i) + " : ")
            if j:
                file2.write(" ".join([f"({col},{val})" for col, val in j]))
            file2.write("\n")
