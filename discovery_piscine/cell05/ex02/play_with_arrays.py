#!/usr/bin/env python3
numbers = [0, 1, 2, 3, 4, 2, 6, 7, 6, 9, 2]
result = []

for number in numbers:
    if number > 5:
        result.append(number + 2)

print(numbers)
print(result)