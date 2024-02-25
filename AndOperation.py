gender=input("Enter gender:")
age=int(input("Enter age:"))
if(gender=="M" or gender=="m" and age>19):
    print("Eligible")
else:
    print("Not Eligible")