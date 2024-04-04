result = []
queue = []
visited = set()
def bfs(G, v, visited, Indeg):
    visited.add(v)
    queue.append(v)

    while queue:
        x = queue.pop(0)
        result.append(x)

        for neighbour in G[x]:
            Indeg[neighbour] -= 1

            if neighbour not in visited and Indeg[neighbour] == 0:
                visited.add(neighbour)
                queue.append(neighbour)


file1 = open('input1b.txt', 'r')
file2 = open('output1b.txt', 'w')

n,m = map(int, file1.readline().split())

my_dict = {}
for i in range(n+1):
    my_dict[i] = []

track = [0]*(n+1)
for i in range(m):
    pre_req,course = map(int, file1.readline().split())
    my_dict[pre_req].append(course)
    track[course] += 1

for i in range(1,n+1):
    if track[i] == 0 and i not in visited:
        bfs(my_dict, i, visited, track)

if len(result) < n:
    file2.write('IMPOSSIBLE')
else:
    file2.write(str(result).strip('[]').replace(',',''))
file1.close()
file2.close()