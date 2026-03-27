roman = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'
}


num = int(input("Enter num: "))

if num < 0:
    print("Error : Please input positive number")
elif num == 0 or num > 9:
    print("Error : out of range")
else:
    ans = roman[num]
    print(ans)