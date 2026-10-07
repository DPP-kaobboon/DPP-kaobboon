#!/usr/bin/env python3
import sys


def downcase_it(text):
    return text.lower()


parameters = sys.argv[1:]
if not parameters:
    print("none")
else:
    for parameter in parameters:
        print(downcase_it(parameter))