#!/usr/bin/env python3
import re
import sys

parameters = sys.argv[1:]

if len(parameters) != 2:
    print("none")
else:
    keyword, text = parameters
    occurrences = len(re.findall(re.escape(keyword), text))
    if occurrences:
        print(occurrences)
    else:
        print("none")