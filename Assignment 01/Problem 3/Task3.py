def selection_sort(arr,id,n):
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if (arr[j] > arr[max_idx]) or (arr[j] == arr[max_idx] and id[j]<id[max_idx]):
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        id[i], id[max_idx] = id[max_idx], id[i]

with open("input1.txt","r") as file:
    n=int(file.readline().strip())
    id = file.readline().strip().split()
    array = file.readline().strip().split()
    selection_sort(array,id,n)
    with open("output1.txt","w") as file2:
        for i in range(n):
            file2.write(f'ID: {id[i]} Mark: {array[i]}\n')
with open("input2.txt","r") as file:
    n=int(file.readline().strip())
    id = file.readline().strip().split()
    array = file.readline().strip().split()
    selection_sort(array,id,n)
    with open("output2.txt","w") as file2:
        for i in range(n):
            file2.write(f'ID: {id[i]} Mark: {array[i]}\n')
            
'''
Here, we employ the selection sort algorithm to arrange students based on their marks, sorting from highest to lowest. 
Also we consider student IDs as preference to lower IDs where marks are same. 

The algorithm iterates through the array, identifying the index of the maximum element
and swaps it with the current position. This process repeats until the entire array is sorted in descending order
with IDs acting as tiebreakers for the same marks.

'''