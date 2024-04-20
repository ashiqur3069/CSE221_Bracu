import heapq

def djikstra(graph, N):
    danger = [float('inf')] * N
    danger[0] = 0
    
    pq = [(0, 0)]
    
    while pq:
        danger, node = heapq.heappop(pq)
        
        if node == N - 1:
            return danger
        
        for v, w in graph[node]:
            new_danger = max(danger, w)
            
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(pq, (new_danger, v))
                
    return "Impossible"

file1 = open('input3.txt', 'r')
file2 = open('output3.txt', 'w')
N, M = map(int, file1.readline().split())
graph = [[] for i in range(N)]

for i in range(M):
    u, v, w = map(int, file1.readline().split())
    graph[u - 1].append((v - 1, w))

result = djikstra(graph, N)

file2.write(str(result) + '\n')
file1.close()
file2.close()