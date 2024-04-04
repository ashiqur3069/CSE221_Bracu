stack = []
visited = set()
def dfs(G, v, visited, Top_sort=True, StrongL = None):
    visited.add(v)
    if not Top_sort:
        StrongL.append(v)

    for neighbour in G[v]:
        if neighbour not in visited:
            dfs(G, neighbour, visited, Top_sort, StrongL)

    if Top_sort:
        stack.append(v)


file1 = open('input3.txt', 'r')
file2 = open('output3.txt', 'w')

n,m = map(int, file1.readline().split())

graph = {}
reverseG = {}
for i in range(n+1):
    graph[i] = []
    reverseG[i] = []

for i in range(m):
    u,v = map(int, file1.readline().split())
    graph[u].append(v)
    reverseG[v].append(u)

for i in range(1,n+1):
    if i not in visited:
        dfs(graph, i, visited)

visited.clear()
strong = []
while stack:
    lst = []
    node = stack.pop()
    if node not in visited:
        dfs(reverseG,node,visited,Top_sort=False,StrongL=lst)

    if lst:
        strong.append(lst)
print(strong)
for i in strong:
    for j in i:
        file2.write(str(j) + " ")
    file2.write("\n")
    
file1.close()
file2.close()