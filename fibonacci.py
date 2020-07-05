numbers = []

for i in range(12):
    if 0 <= i-2 < len(numbers):
        numbers.append(numbers[i-1]+numbers[i-2])
    else:
        numbers.append(1)

print(numbers)
exit()