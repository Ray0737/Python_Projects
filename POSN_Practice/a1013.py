char = input("Enter char code: ")
num = int(input("Enter 4 digit code: "))

correct_char = "H"
correct_num = 4567

if char == correct_char and num != correct_num:
    print("safe locked - change digit")

elif char != correct_char and num == correct_num:
    print("safe locked - change char")

else:
    print("safe locked")