#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

if not parameters:
    print("none")
else:
    print(f"parameters: {len(parameters)}")
    for parameter in parameters:
        print(f"{parameter}: {len(parameter)}")