#!/usr/bin/env python3
import sys


def shrink(text):
    print(text[:8])


def enlarge(text):
    print(text + "Z" * (8 - len(text)))


parameters = sys.argv[1:]
if not parameters:
    print("none")
else:
    for parameter in parameters:
        if len(parameter) > 8:
            shrink(parameter)
        elif len(parameter) < 8:
            enlarge(parameter)
        else:
            print(parameter)