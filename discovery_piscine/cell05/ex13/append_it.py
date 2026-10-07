#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

if not parameters:
    print("none")
else:
    for parameter in parameters:
        if not parameter.endswith("ism"):
            print(f"{parameter}ism")