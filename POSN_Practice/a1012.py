num = int(input("Enter num (10-99): "))
operator = input("Enter operator (+ or *): ")
new = ""

if 10 <= num <= 99:
    for i in reversed(str(num)):
        new += i
    if operator == "+":
        print(f"{num} + {new} = {num + int(new)}")
    elif operator == "*":
        print(f"{num} * {new} = {num * int(new)}")