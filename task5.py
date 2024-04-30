n = int(input())


for num in range(1, n + 1):
    for i in range(n, num - 1, -1):
        print(num, end=' ')
    print()
