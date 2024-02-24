def partition(a, p, r):
  x = a[r]
  i = p-1
  for j in range(p, r, 1):
    if a[j] < x:
      i += 1
      a[i], a[j] = a[j], a[i]
  a[i+1], a[r] = a[r], a[i+1]
  return i+1

def find_Kth_Smallest(a, k):
  p = 0
  r = len(a)-1
  while p <= r:
    pivot_idx = partition(a, p, r)
    if pivot_idx == k-1:
      return a[pivot_idx]
    elif pivot_idx > k-1:
      r = pivot_idx-1
    else:
      p = pivot_idx+1
  return None

with open("input6.txt","r") as file:
    size = int(file.readline()[0])
    array = file.readline().split(" ")
    array = list(map(int, array))
    queries = int(file.readline()[0])
    with open("output6.txt","w") as file2:
        for i in range(queries):
            kth = int(file.readline())
            smallest_num = find_Kth_Smallest(array, kth)
            file2.write(str(smallest_num)+"\n")