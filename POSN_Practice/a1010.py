age = int(input("Enter age: "))
status = input("Enter status: ").strip().lower()

if age < 18 or status == "s":
    print("20")
else:
    print("50")