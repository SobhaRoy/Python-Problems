str1=input("Enter a string:")
str2=input("Enter another string:")
new_str1=str1.split()
new_str2=str2.split()
for i in new_str2:
    if i not in new_str1:
        print(i)
