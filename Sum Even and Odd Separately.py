n=int(input("how many no you check:"))
i=1
s=0
su=0
while(i<=n):
    print("Enter the no:")
    num=int(input())
    if(num%2==0):
        s=s+num
        i+=1
    else:
        su=su+num
        i+=1
    print("Two integers: even sum:",s,"odd sum:",su)
