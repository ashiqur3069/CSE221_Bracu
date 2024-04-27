def getParent(parent, n):
  par = parent[n]
  if par==n:
    return par
  else:
    return getParent(parent, par)

file1 = open("input1.txt", "r")
fine2 = open("output1.txt", "w")

main = list(filter(None, file1.read().split("\n")))


input = main[0].split(" ")
n = int(input[0])
k = int(input[1])

parent = [i for i in range(n + 1)]
friends = [1]*(n+1)

for i in range(1, len(main),1):
    data = main[i].split(" ")
    node1 = int(data[0])
    node2 = int(data[1])

    parent1 = getParent(parent, node1)
    parent2 = getParent(parent, node2)

    if (parent1!=parent2):
        parent[node2] = parent1
        parent[parent2] = parent1
        friends[parent1]= friends[parent1]+friends[parent2]
    fine2.write(str(friends[parent1]))
    if i<len(main)-1:
       fine2.write("\n")
file1.close()
fine2.close()