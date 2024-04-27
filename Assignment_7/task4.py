def coinChange(coins, amount):
    queue = [(0, 0)]
    visited = set()
    
    while queue:
        sum_num, steps = queue.pop(0)
        if sum_num == amount:
            return steps
        for coin in coins:
            next_sum = sum_num + coin
            if next_sum <= amount and next_sum not in visited:
                queue.append((next_sum, steps + 1))
                visited.add(next_sum)
    return -1

file1 = open("input4.txt", "r")
main = file1.read().split("\n")
line1 = main[0].split(" ")
n = int(line1[0])
x = int(line1[1])
line2 = main[1].split(" ")
coins = [int(c) for c in line2]

result = coinChange(coins, x)

file2 = open("output4.txt", "w")
file2.write(str(result))
file1.close()
file2.close()
