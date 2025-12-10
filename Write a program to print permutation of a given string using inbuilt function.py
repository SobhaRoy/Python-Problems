from itertools import permutations
str1=input("Enter a string:")
p=permutations(str1)
for i in p:
    print(''.join(i))
