sales = [
    [5, 3, 0, 2],
    [7, 0, 2, 1],
    [0, 1, 4, 0]
]

max=-1
min= float('inf')
for col in range(len(sales[0])):   # loop through columns
    s = 0
    for row in range(len(sales)):  # loop through rows
        s += sales[row][col]
    if(max<s):
        max=s
        loc1=col
    if(min>s):
        min=s
        loc2=col
    
    print("product",col+1,"sale is",s)
print("max value ",max," product",loc1+1)
print("min value ",min, " product",loc2+1)

