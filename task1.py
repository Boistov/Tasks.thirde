def calculate_sum(n):
    total = 0
    v = 0

    for i in range(1, n + 1):
        v = v * 10 + 2
        total += v

    return total
n = int(input())

sum = calculate_sum(n)
print(sum)
