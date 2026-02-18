l=[1,2,3,4]
for i in range(0,len(l)):
    new_list=l[:i]+l[i+1:]
    print(new_list)
