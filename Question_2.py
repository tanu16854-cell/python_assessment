# Q2. Develop a grading system where marks of five subjects are entered by the user. The program should
# calculate percentage, assign grades using nested if-else conditions, and identify whether the student qualifies for
# a scholarship

marks = []

for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("\nPercentage:", percentage)

# Grade calculation using nested if-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Scholarship condition
if percentage >= 85:
    scholarship = "Eligible"
else:
    scholarship = "Not Eligible"

print("Grade:", grade)
print("Scholarship:", scholarship)