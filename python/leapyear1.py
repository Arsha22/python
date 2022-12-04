i=int(input("enter the current year:"))
j=int(input("enter the year to which the leapyear has to be printed:"))
for i in range(i,j+1):
            if((i%4==0)and(i%100!=0)or(i%400==0)):
                print(i,"-leapyear")
            else:
                print(i)
                
