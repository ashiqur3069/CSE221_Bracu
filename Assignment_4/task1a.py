def create_matrix(N, M, edges):
    adj_matrix = [[0] * N for i in range(N)]
    for edge in edges:
        row, col, val = edge
        adj_matrix[row][col] = val
    return adj_matrix

with open("input1a.txt","r") as file:
    N, M = map(int, file.readline().split())
    edges = []
    for i in range(M):
        row, col, val = map(int, file.readline().split())
        edges.append((row, col, val))
    output = create_matrix(N+1,M+1,edges)
    with open("output1a.txt","w") as file2:
        for row in output:
            file2.write(" ".join(map(str, row)) + "\n")
