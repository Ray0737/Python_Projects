firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
age = input("Enter age: ")

text = ""
if len(firstname) >5:
    text += firstname[0:2]
    text += lastname[-1]
    text += age[-1]
else:
    text += firstname[0:1]
    text += age
    text += lastname[-1]
print(text)