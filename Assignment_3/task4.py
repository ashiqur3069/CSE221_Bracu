def merge(arr):
    if len(arr) <= 1:
        return arr, int(arr[0])
    else:
        mid = len(arr) // 2
        left, max_val = merge(arr[:mid])
        right, max_val = merge(arr[mid:])
        merged, max_val = mergeSort(left, right, max_val)
        return merged, max_val

def mergeSort(left, right, max_val):
    i, j = 0, 0
    while i < len(left) and j < len(right):
        calculate = left[i] + right[j]**2
        max_val = max(max_val, calculate)
        if left[i] <= right[j]:
            i += 1
        else:
            j += 1
    return left+right, max_val



with open("input4.txt","r") as file:
    size = int(file.readline())
    array = file.readline().split(" ")
    array = list(map(int, array)) 
    sorted, max_value = merge(array)
    print(max)    
    with open("output4.txt","w") as file2:
            file2.write(f"{max_value}")