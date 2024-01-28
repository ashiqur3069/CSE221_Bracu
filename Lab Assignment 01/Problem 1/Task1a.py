with open("input1a.txt","r") as file:
    next(file)
    with open("output1a.txt","w") as file2:
        for line in file:
            number = line.strip()
            if int(number) % 2 == 0:
                file2.write(f"{number} is an Even number.\n")
            else:
                file2.write(f"{number} is an odd number.\n")
