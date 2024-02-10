
def marge_list(array):
    return sorted(array)
with open("input2.txt","r") as file:
    size1 = file.readline()
    list1 = file.readline().strip().split()
    size2 = file.readline()
    list2 = file.readline().strip().split()

    array = []
    for i in list1:
        array.append(int(i))
    for j in list2:
        array.append(int(j))
    output = marge_list(array)

    with open("output2.txt", "w") as file2:

        for i in output:
            file2.write(f"{i} ")
