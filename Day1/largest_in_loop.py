# Find the largest number in the list [9, 41, 12, 3, 74, 15]

largest = None
for value in [9,41,12,3,74,15]:
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
print('largest number is', largest
