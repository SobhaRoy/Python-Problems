str1=input("Enter a string:")
length=len(str1)
vowels='aeiouAEIOU'
flag=1
for i in range(0,length):
    if str1[i] not in vowels:
        flag=0
        break
if flag==1:
    print("ALL VOWELS")
else:
    print("all char is not vowels")
    
