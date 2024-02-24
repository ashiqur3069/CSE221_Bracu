def merge(a, b):
       
    new_array = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if int(a[i]) < int(b[j]):
            new_array.append(int(a[i]))
            i += 1
        else:
            new_array.append(int(b[j]))
            j += 1
    new_array += a[i:]
    new_array += b[j:]
    return new_array



def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  
        a2 = mergeSort(arr[mid:]) 
        return merge(a1, a2) 
with open("input1.txt","r") as file:
    size = file.readline()
    array = file.readline().strip().split()
    output = mergeSort(array)
    with open("output1.txt","w") as file2:
        for i in output:
            file2.write(f"{i} ")