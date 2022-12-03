import random

numbers = []

for i in range(5):
    numbers.append(random.randrange(1,10))

print(numbers)

i = len(numbers) - 1
while i > 1:
    j = 0

    while j < i:
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
        else:
            print()
        j += 1
    i -= 1

for k in numbers:
    print(k, end=", ")
print()