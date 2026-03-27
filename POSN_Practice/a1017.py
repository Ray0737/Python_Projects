year1 = input("Enter year: ")
month1 = input("Enter month: ")
day1 = input("Enter Dat: ")

year2= input("Enter year: ")
month2 = input("Enter month: ")
day2 = input("Enter Dat: ")

if year1 < year2: # p1 is older
    print("1")
elif year1 > year2:
    print("2")
elif year1 == year2:
    if month1 < month2:
        print("1")
    elif month1 > month2:
        print("2")
    elif month1 == month2:
        if day1 < day2:
            print("1")
        if day1 > day2:
            print("2")
        if day1 == day2:
            print("0")
