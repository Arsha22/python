string=input("enter the two string separated by comma:")
string=string.split(',')
print(string[1][0]+string[0][1:]+" "+string[0][0]+string[1][1:])
