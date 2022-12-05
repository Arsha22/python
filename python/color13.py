count=int(input("how much colors:"))
colorlist=[]
for i in range(count):
    color=input("enter the color:")
    colorlist.append(color)
print(colorlist[0]," ",colorlist[-1])
