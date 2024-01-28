with open("input1b.txt", "r") as file:
    next(file)
    with open("output1b.txt", "w") as file2:
        for line in file:
            t = line.strip()
            t = t.split(" ")
            operator = t[2]
            operand1 = int(t[1])
            operand2 = int(t[3])
            if operator == '+':
                result = operand1 + operand2
                file2.write(f"The result of {operand1} + {operand2} is {result}\n")

            elif operator == '-':
                result = operand1 - operand2
                file2.write(f"The result of {operand1} - {operand2} is {result}\n")
            elif operator == '*':
                result = operand1 * operand2
                file2.write(f"The result of {operand1} * {operand2} is {result}\n")

            elif operator == '/':
                result = operand1 / operand2
                file2.write(f"The result of {operand1} / {operand2} is {result}\n")

            else:
                file2.write(f"The operator is invalid.\n")

