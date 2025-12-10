str1=input("Enter a string:")
result=''
for ch in str1:
    if ch==',':
        result+='.'
    elif ch=='.':
        result+=','
    else: result+=ch
print(result)
