# Q5: Second largest and second smallest

def find_second(arr):
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in arr:
        # largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

        # smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest, second_largest


nums = list(map(int, input("Enter numbers: ").split()))
s_small, s_large = find_second(nums)

print("Second Smallest:", s_small)
print("Second Largest:", s_large)