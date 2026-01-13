import re
st1="this is first line far of fat code"
b="my phone number is 988^3057767"
c="My DOB is 07/05/1983"
d="mca bcabbbbb mcamca mba bcabba mcaa"
e="my email id is tmp.manna@gmail.com"
match=re.findall("f",st1)
print(match)

'''match=re.search("98",b)
print(match)

match=re.findall("[b-f]",st1)
print(match)

match=re.findall("[0-9]",b)
print(match)

match=re.findall("[apq]",b)
print(match)

match=re.search("^m",e)
print(match)

match=re.search("m$",e)
print(match)'''

match=re.search("b{2}",d)
print(match)

match=re.findall("b{2,4}",d)
print(match)

match=re.search("[0-9]+",c)
print(match)




#re.findall(pattern,string)
#re.search()




