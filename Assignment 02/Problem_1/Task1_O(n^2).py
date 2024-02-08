def two_sum(array,size,value):
    for i in range(size):
        for j in range(i + 1, size):
            if int(array[i]) + int(array[j]) == value:
                return list((i+1,j+1))
    return None


with open("input1.txt","r") as file:
    n1 = file.readline().strip().split()
    n2 = file.readline().strip().split()
    output = two_sum(n2,int(n1[0]),int(n1[1]))
    with open("output1.txt", "w") as file2:
            if output is not None:
                file2.write(f"{output[0]} {output[1]}")
            else:
                file2.write("Impossible")


