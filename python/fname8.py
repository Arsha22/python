namelist=[]
len=int(input("how many names do you want to enter:"))
for item in range(0,len):
    fname=input("enter the first name:")
    namelist.append(fname)
    count_a=0
for names in namelist:
    count_a+=names.count("a")
print(count_a)
