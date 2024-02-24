def finding_max(array,left,right):
    if left == right:
        return array[left]
    mid = (left + right) // 2
    print(mid)
    left_max = finding_max(array,left,mid)
    right_max = finding_max(array,mid + 1, right)

    return max(left_max,right_max)
with open("input2.txt","r") as file:
    size = file.readline()
    array = file.readline().strip().split()
    new_array = []
    for i in array:
        new_array.append(int(i))
    output = finding_max(new_array,0,int(size)-1)
    with open("output2.txt","w") as file2:
            file2.write(f"{output}")