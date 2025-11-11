n=int(input("Enter the size:"))
i=1
c=0
while(i<=n):
    num=int(input("Enter a no:"))
    if(c==0):
        if(num%2==0):
            print(num)
            c=1
        else:
            if(num%2!=0):
                print(num)
                c=1
