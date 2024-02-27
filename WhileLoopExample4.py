elements=(1,2,3,4,5,6,7,8,9)
x=5
i=0
while i<len(elements):
    if(elements[i]==x):
        print("index: ",i)
        break
    else:
        i+=1