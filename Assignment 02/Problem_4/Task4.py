def maximum_task(array,task,person):
    array.sort(key = lambda x : int(x[1]))
    new_array = [0] * person
    count = 0
    for start, end in array:
        index = 0
        min = 24
        flag = False
        for i in range(person):
            if new_array[i]== int(start) and not flag:
                new_array[i] = int(end)
                count+=1
                break

            elif new_array[i] == 0:
                new_array[i] = int(end)
                count+=1
                break
            elif int(start) >= new_array[i] and min >= (int(end) - new_array[i]):
                min = (int(end) - new_array[i])
                index = i
                flag = True
        if flag:
            new_array[index] = int(end)
            count += 1

    return count

with open("input4.txt","r") as file:
    input = file.readlines()
    size = input[0].split()
    task = int(size[0])
    person = int(size[1])
    array = []
    for i in range(1,task+1):
        array.append(input[i].strip().split(' '))
    output = maximum_task(array,task,person)
    with open("output4.txt", "w") as file2:
        file2.write(f"{output}")
