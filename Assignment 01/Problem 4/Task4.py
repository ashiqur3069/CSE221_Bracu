def bubbleSort(array):
  for i in range(n):
    for j in range(n - i - 1):
      tr1=array[j].strip().split()
      tr2=array[j+1].strip().split()
      if (tr1[0] > tr2[0]) or (tr1[0] == tr2[0] and tr1[-1].replace(":",'') < tr2[-1].replace(":",'')):
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

with open("input.txt","r") as file:
    n=int(file.readline().strip())
    arr = file.readlines()
    bubbleSort(arr)
    with open("output.txt","w") as file2:
        file2.writelines(arr)
'''
Comment:

Here we do bubble sort while comparing the lexicographical order based on the name of the trains.
Also when name of train is same then we compared with the lastest departure time while int of time is greater
then the other, we prioritized the train based on that also so we needs two conditions to check.

'''
            