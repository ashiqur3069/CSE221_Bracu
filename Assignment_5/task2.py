import heapq

result = []
visited = set()
priority_queue = []
heapq.heapify(priority_queue)

def bfs(G, v, visited, track):
    visited.add(v)
    heapq.heappush(priority_queue,v)

    while priority_queue:
        node = heapq.heappop(priority_queue)
        result.append(node)

        for neighbour in G[node]:
            track[neighbour] -= 1

            if neighbour not in visited and track[neighbour] == 0:
                visited.add(neighbour)
                heapq.heappush(priority_queue,neighbour)
file1 = open('input2.txt', 'r')
file2 = open('output2.txt', 'w')

n,m = map(int, file1.readline().split())

my_dict = {}
for i in range(n+1):
    my_dict[i] = []

track = [0]*(n+1)
for i in range(m):
    s,d = map(int, file1.readline().split())
    my_dict[s].append(d)
    track[d] += 1

for i in range(1,n+1):
    if track[i] == 0 and i not in visited:
        bfs(my_dict, i, visited, track)
if len(result) < n:
    file2.write('IMPOSSIBLE')
else:
    file2.write(str(result).strip('[]').replace(',',''))

file1.close()
file2.close()