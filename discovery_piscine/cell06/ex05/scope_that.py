#!/usr/bin/env python3


def add_one(number):
    number = number + 1
    print(f"Inside add_one method: {number}")

my_number = 10

print(f"Before method call: {my_number}")

add_one(my_number)

print(f"After method call:  {my_number}")