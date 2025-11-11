# Program to calculate fine for late book return

days = int(input("Enter number of days book is returned late: "))

if days <= 5:
    fine = days * 0.5
    print("Fine is Rs.", fine)
elif days <= 10:
    fine = (5 * 0.5) + (days - 5) * 1
    print("Fine is Rs.", fine)
elif days <= 30:
    fine = (5 * 0.5) + (5 * 1) + (days - 10) * 5
    print("Fine is Rs.", fine)
else:
    print("Membership cancelled.")
