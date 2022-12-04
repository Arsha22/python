len=int(input("how many numbers do you want to store"))
valuelist=[]
for num in range(0,len):
    invalue=int(input("enter value"))
    if(invalue>100):
        valuelist.append('over')
    else:
        valuelist.append(invalue)
print(valuelist)
