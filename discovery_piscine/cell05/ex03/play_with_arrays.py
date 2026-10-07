#!/usr/bin/env python3
numbers = [2, 4, 6, 8, 10, 12, 14, 6, 18, 2]
result = set()

for number in numbers:
    if number > 5:
        result.add(number + 2)

print(numbers)
print(result)