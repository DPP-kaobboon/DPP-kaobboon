#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

if len(parameters) != 2:
    print("none")
else:
    start, end = (int(parameter) for parameter in parameters)
    numbers = list(range(start, end + 1))
    print(numbers)