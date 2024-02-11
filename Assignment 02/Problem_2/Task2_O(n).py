def marge_list(size1,size2,list1,list2):
    array = []
    i, j = 0, 0
    while i < int(size1) and j < int(size2):
        if int(list1[i]) < int(list2[j]):
            array.append(list1[i])
            i += 1
        else:
            array.append(list2[j])
            j+= 1
    array += list1[i:]
    array += list2[j:]
    return array

with open("input2.txt","r") as file:
    size1 = file.readline()
    list1 = file.readline().strip().split()
    size2 = file.readline()
    list2 = file.readline().strip().split()
    output = marge_list(size1,size2,list1,list2)
    with open("output2.txt", "w") as file2:
        for i in output:
            file2.write(f"{i} ")
