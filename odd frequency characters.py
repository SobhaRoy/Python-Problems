str1=input("Enter a string:")
for i in str1:
    if(str1.count(i)%2!=0):
        odd=str1.count(i)
result=''
for i in str1:
    if str1.count(i)==odd and i not in result:
        result=result+i
for i in result:
    print(i)
