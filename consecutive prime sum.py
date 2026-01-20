n=50
s=0
for i in range(2,n+1):
    c=0
    p=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        s=s+i
        if s!=2:
            if s<=n:
                for k in range(1,s+1):
                    if s%k==0:
                        p+=1
                if p==2:
                    print(s)
                        

        
