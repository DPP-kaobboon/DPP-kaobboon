#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
else:
    table = 0
    while table <= 10:
        products = []
        multiplier = 0
        while multiplier <= 10:
            products.append(str(table * multiplier))
            multiplier += 1
        print(f"Table de {table}: {' '.join(products)}")
        table += 1