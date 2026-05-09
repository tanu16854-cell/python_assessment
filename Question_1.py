# Q1. Write a Python program that accepts a paragraph from the user and calculates the number of uppercase
# letters, lowercase letters, digits, spaces, and special characters. Display the result in descending order based on
# frequency

text = input("Enter a paragraph: ")

upper = lower = digits = spaces = special = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

result = {
    "Uppercase": upper,
    "Lowercase": lower,
    "Digits": digits,
    "Spaces": spaces,
    "Special Characters": special
}

# Sorting by frequency (descending)
sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

print("\nCharacter Frequency (Descending Order):")
for k, v in sorted_result.items():
    print(k, ":", v)