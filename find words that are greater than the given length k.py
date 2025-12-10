str1=input("Enter a string:")
k=int(input("given length of k:"))
str2=str1.split()
for i in str2:
    l=len(i)
    if l>k:
        print (i)
