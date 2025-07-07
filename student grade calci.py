marks = []
subjects = int(input("Enter number of subjects: "))
for i in range(subjects):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / subjects

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Total: {total}, Average: {average:.2f}, Grade: {grade}")
