n=int(input("Enter the size:"))
i=1
c=0
k=int(input("Enter k value:"))
while(i<=n):
    num=int(input("Enter no:"))
    if(i==1):
        i+=1
    else:
        i+=1
        if(num%k==0):
            print(num,"multiplies by",k)
            c+=1
print("total multiply value",c)
