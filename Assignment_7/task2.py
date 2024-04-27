def getParent(parent, n):
  par = parent[n]
  if par==n:
    return par
  else:
    return getParent(parent, par)

file1 = open("input2.txt", "r")
file2 = open("output2.txt", "w")

main = file1.read().split("\n")

line1 = main[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])

c = []
graph = []
parent = [0]* (nodes+1)
totalCost = 0

parent = [i for i in range(nodes + 1)]

for i in range(1, len(main)-1, 1):
  info = main[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  cost = int(info[2])
  lst = [node1, node2, cost]
  c.append(lst)

conn = sorted(c, key=lambda x: x[2])

for i in range(len(conn)):
  node1 = conn[i][0]
  node2 = conn[i][1]
  cost = conn[i][2]

  parent1 = getParent(parent, node1)
  parent2 = getParent(parent, node2)

  if (parent1!=parent2):
    parent[node2] = parent1
    parent[parent2] = parent1
    graph.append(conn[i])
    totalCost+=cost

file2.write(str(totalCost))
file1.close()
file2.close()
