def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        return 1
    else:
        return 0
    
n=int(input("Enter a num:"))
p=perfect(n)
if p==1:
    print("perfect")
else:
    print("not perfect")
