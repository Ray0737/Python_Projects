winter = [1,2,3]
spring = [4,5,6]
summer = [7,8,9]
fall = [10,11,12]

month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month in winter and (day < 21):
    print("Winter")
elif month in spring and (day < 21):
    print("Spring")
elif month in summer and (day < 21):
    print("Summer")
elif month in fall and (day < 21):
    print("Fall")
elif day >= 21 and month == winter[-1]:
    print("Spring")
elif day >= 21 and month == spring[-1]:
    print("Summer")
elif day >= 21 and month == summer[-1]:
    print("Fall")
elif day >= 21 and month == fall[-1]:
    print("Winter")
