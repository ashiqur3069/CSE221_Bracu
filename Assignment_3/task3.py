def Merge(left, right):
  new_arr = []
  count = 0
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      new_arr.append(left[i])
      count += len(right) - j
      i += 1
    else:
      new_arr.append(right[j])
      j += 1

  new_arr.extend(left[i:])
  new_arr.extend(right[j:])
  return new_arr, count

def mergeSort(arr):
  if len(arr) <= 1:
    return arr, 0
  else:
    mid = len(arr) // 2
    left, count_left = mergeSort(arr[:mid])
    right, count_right = mergeSort(arr[mid:])
    sorted_arr, count = Merge(left, right)
    total_count = count_left + count_right + count
    return sorted_arr, total_count

with open("input3.txt","r") as file:
    size = file.readline()
    array = file.readline().split(" ")
    array = list(map(int, array)) 
    sorted_array, count = mergeSort(array)
    print(count)
    
    with open("output3.txt","w") as file2:
            file2.write(f"{count}")