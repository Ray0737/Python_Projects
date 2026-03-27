withdraw = int(input("Enter Amount: "))
ten = withdraw // 10
five = (withdraw % 10) // 5
two = ((withdraw % 10) % 5) // 2
one = (((withdraw % 10) % 5) % 2) // 1
print(f"10 = {ten}\n5 = {five}\n2 = {two}\n1 = {one}")