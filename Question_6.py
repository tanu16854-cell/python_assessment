# Q8. Write a Python program to perform union, intersection, symmetric difference, and subset operations on two
# sets entered by the user
set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Symmetric Difference:", set1 ^ set2)
print("Is Subset:", set1.issubset(set2))
