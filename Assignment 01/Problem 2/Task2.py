
def bubbleSort(arr):
    flag = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1): 
            arr[j],array[j+1] = int(arr[j]), int(arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            return
with open("input2a.txt","r") as file:
    next(file)
    array = file.read().strip().split()
    bubbleSort(array)
    with open("output2a.txt","w") as file2:
        file2.write(f'{array}')
with open("input2b.txt","r") as file:
    next(file)
    array = file.read().strip().split()
    bubbleSort(array)
    with open("output2b.txt","w") as file2:
        file2.write(f'{array}')
'''
In the best-case scenario:
We initialize a variable flag to False
The outer loop iterates only 1 time and the inner loop iterates n time for checking if every element is in unsorted order.
If elements in sorted order then flag is set to be True and return and stop the function.
So The time complexity in thee best case scenario is O(n)

'''
