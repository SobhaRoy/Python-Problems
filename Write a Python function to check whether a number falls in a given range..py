def given_range(n):
    flag=0
    for i in range(1,11):
        if n==i:
            print(n,"is in the range")
            flag=1
    if flag==0:
        print(n,"is not in range")
n=int(input("enter a no:"))
given_range(n)
