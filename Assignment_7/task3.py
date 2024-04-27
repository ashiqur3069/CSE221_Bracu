def fib(n):
    if storage[n]:
        return storage[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        storage[n] = result
        return result

file1 = open("input3.txt", "r")
file2 = open("output3.txt", "w")
main = int(file1.read())
storage = {i:[] for i in range(main+2)}
file2.write(str(fib(main+1)))
file1.close()
file2.close()