import heapq as hq
import math

def djikstra(graph, source):
    distance = [math.inf]*len(graph)
    visited = [False]*len(graph)
    prev = [None]*len(graph)
    distance[source] = 0
    q = []
    hq.heappush(q,(distance[source],source))
    print(q)


    while q:
        num, u = hq.heappop(q)
        if visited[u] == True:
           continue
        visited[u] = True
        for v,cost in graph[u]:
            new_cost = distance[u] + cost
            if new_cost < distance[v]:
                distance[v] = new_cost
                prev[v] = u
                hq.heappush(q, (distance[v], v))

    distance.pop(0)
    while math.inf in distance:
        idx = distance.index(math.inf)
        distance[idx] = -1
    return distance



file1 = open("input1.txt", "r")
file2 = open("output1.txt", "w")
input = file1.read().split("\n")
line1 = input[0].split(" ")
num_of_node = int(line1[0])
num_of_edges = int(line1[1])
sourse_node = int(input[-1])

my_dict = {i:[] for i in range(num_of_node+1)}
for i in range(1,len(input)-1,1):
    line = input[i].split(" ")
    node1 = int(line[0])
    node2 = int(line[1])
    cost = int(line[2])
    array = my_dict[node1]
    array.append((node2,cost))


main = djikstra(my_dict,sourse_node)
file2.write(" ".join(list(map(str, main))))
file1.close()
file2.close()