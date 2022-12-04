word=input("enter the word:")
vowel=['a','e','i','o','u']
newlist=[]
for x in word:
    if(x in vowel and x not in newlist):
        newlist.append(x)
print(newlist)
