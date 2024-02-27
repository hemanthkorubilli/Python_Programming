x=int(input("Enter value to search:"))
tuple=(1,2,3,5,6,8,9)
for i in range(0,len(tuple)):
    if(tuple[i]==x):
        print("Item found")
        break
else:
    print("For loop ended but item",x ,"not found")
        

