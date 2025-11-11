i = 1
while i <= 5:
    emp_hour = int(input("How many hours the employee worked: "))
    if emp_hour > 40:
        pay = emp_hour - 40
        pay1 = pay * 12
        print("Extra pay for the employee is:", pay1)
    else:
        print("No overtime pay")
    i += 1
