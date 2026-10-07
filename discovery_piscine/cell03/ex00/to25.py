#!/usr/bin/env python3
number = int(input("Please enter a number: "))
if number > 25:
    print("ERROR")
else:
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1