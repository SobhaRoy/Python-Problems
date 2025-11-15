c=0
s=0
count=0
while(True):
    n=int(input("Enter no:"))
    c=0
    count+=1
    while(n>9):
        s=0
        while(n!=0):
            r=n%10
            s=s+r
            n=n//10
        n=s
        c+=1
    print("The final single digit result:",n)
    print("Iteration",c)
    ch=int(input("For continution press 1 for stop press 0 or negative for stop"))
    if(ch==0 or ch<0):
        print("You are outer of the loop")
        break
print("Total numbers processed",count)
