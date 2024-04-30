numbers = [112, 75, 150, 100, 145, 525, 50]

for num in numbers:
    if num % 5 == 0:
        if num > 150:
            continue
        elif num > 500:
            break
        else:
            print(num)



