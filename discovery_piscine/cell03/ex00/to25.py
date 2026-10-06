number = int(input("Enter a number: "))
if number > 25:
    print("Error")
if number <= 25:
    for count in range(number, 26):
        print(f"Inside the loop, my variable is {count}")