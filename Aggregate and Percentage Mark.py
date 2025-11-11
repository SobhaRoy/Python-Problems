# Aggregate and Percentage Marks
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Percentage:", percentage, "%")
