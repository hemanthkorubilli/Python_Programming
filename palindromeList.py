lst=[1,2,3,2,1]
lst1=lst.copy()
lst.reverse()
if(lst==lst1):
    print("Palindrome")
else:
    print("Not a palindrome")