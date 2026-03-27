list = ["a","e","i","o","u"]
letter = input("Enter 1 letter: ").strip().lower()

if letter in list and len(letter) == 1:
    print("Yes")
else:
    print("No")