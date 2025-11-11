# Program to check insurance eligibility and premium

health = input("Enter health condition (excellent/poor): ").lower()
age = int(input("Enter age: "))
sex = input("Enter sex (male/female): ").lower()
city = input("Enter place of residence (city/village): ").lower()

if health == "excellent" and 25 <= age <= 35 and city == "city" and sex == "male":
    rate = 4
    max_amount = 200000
    print("Insured at Rs.", rate, "per thousand. Max policy:", max_amount)
elif health == "excellent" and 25 <= age <= 35 and city == "city" and sex == "female":
    rate = 3
    max_amount = 100000
    print("Insured at Rs.", rate, "per thousand. Max policy:", max_amount)
elif health == "poor" and 25 <= age <= 35 and city == "village" and sex == "male":
    rate = 6
    max_amount = 10000
    print("Insured at Rs.", rate, "per thousand. Max policy:", max_amount)
else:
    print("Person is not insured.")
