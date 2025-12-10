from difflib import get_close_matches
l=['cat','car','bike','cow']
s=input("Enter a string:")
match=get_close_matches(s,l,n=len(l),cutoff=1.0)
print(match)
