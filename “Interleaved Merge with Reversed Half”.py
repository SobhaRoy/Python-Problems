str1=input("Enter fst string:")
str2=input("Enter 2nd string:")
result=''
str1_l=len(str1)
str2_l=len(str2)
min1=min(str1_l,str2_l)
for i in range(0,min1):
    result+=str1[i]
    result+=str2[str2_l -1 -i]
print(result)
if str1_l>str2_l:
    result+=str1[min1:]
elif str1_l<str2_l:
    res=str2[:str2_l - min1]
    result+=res[::-1]
print(result)
    
