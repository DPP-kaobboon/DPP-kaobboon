#!/usr/bin/env python3
import sys

def display_first_parameter():
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("Non.")

display_first_parameter()   