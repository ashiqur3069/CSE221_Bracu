def maximum_task(array):
    array.sort(key = lambda x : int(x[1]))
    new_array = []
    pre_end = -1
    for start, end in array:
        if int(start) >= int(pre_end):
            new_array.append([start,end])
            pre_end = end
    return new_array

with open("input3.txt","r") as file:
    input = file.readlines()
    size = int(input[0])
    array = []
    for i in range(1,size+1):
        array.append(input[i].strip().split(' '))
    output = maximum_task(array)
    with open("output3.txt", "w") as file2:
        file2.write(f"{len(output)}\n")
        for i, j in output:
            file2.write(f"{i} {j}\n")

