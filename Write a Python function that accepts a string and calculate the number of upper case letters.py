def check_up_lw(s):
    u_c=0
    l_c=0
    for i in s:
        if i.isupper():
            u_c+=1
        else:
            l_c+=1
    print("upper case letter is ",u_c)
    print("lower case letter is ",l_c)

s=input("Enter a string:")
check_up_lw(s)
