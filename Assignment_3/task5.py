def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)
    return array

def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

with open("input5.txt","r") as file:
    size = int(file.readline())
    array = file.readline().split(" ")
    array = list(map(int, array))
    output = quicksort(array,0,size-1)
    with open("output5.txt","w") as file2:
        for i in output:
            file2.write(f"{i} ")
