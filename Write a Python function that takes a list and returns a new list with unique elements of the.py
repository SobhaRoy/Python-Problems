def unique_list(l):
    new_list=[]
    for i in range(0,len(l)):
        if l[i] not in new_list:
            new_list.append(l[i])
    return new_list


l=[1,2,1,3,4,2,3,5,4,1]
print(unique_list(l))
