number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
result = number_one * number_two
print(f"{number_one} x {number_two} = {result}")
if result == 0:
    print("The result is equal to zero.")
if result > 0:
    print("The result is positive.")
if result < 0:
    print("The result is negative.")