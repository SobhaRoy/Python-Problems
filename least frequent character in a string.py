str1=input("Enter a string:")
min=str1.count(str1[0])
for i in str1:
    c=str1.count(i)
    if c<min:
        min=c
        
result=''
for i in str1:
    if str1.count(i)==min and i not in result:
        result=result+i
for i in result:
    print(i)
