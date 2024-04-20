import heapq

def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


file1 = open('input2.txt', 'r')
file2 = open('output2.txt', 'w')

N,M = map(int, file1.readline().split())

graph = {}

for i in range(N+1):
    graph[i] = []

for i in range(M):
    s,d,w = map(int, file1.readline().split())
    graph[s].append((d,w))

s,t = map(int, file1.readline().split())

dS = dijkstra(graph, s)
dT = dijkstra(graph, t)

min_time = float('inf')
Meet = None

for v in range(1, N + 1):
    if dS[v] != float('inf') and dT[v] != float('inf'):
        t = max(dS[v] , dT[v])
        if t < min_time:
            min_time = t 
            Meet = v

if Meet == None or min_time == float('inf'):
    file2.write('Impossible')
else:
    file2.write(f"Time {min_time} \nNode {Meet}")

file1.close()
file2.close()