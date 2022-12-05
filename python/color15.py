colorlist1=[]
colorlist2=[]
colorlist3=[]
a=int(input("how many colorsdo you want to enter colorlist1:"))
for i in range(a):
    color1=input("enter the color:")
    colorlist1.append(color1)
b=int(input("enter the colors to insert in colorlist2:"))
for i in range(b):
    color2=input("enter the color:")
    colorlist2.append(color2)
colorlist3=[each for each in colorlist1 if each not in colorlist2]
print(colorlist3)
