#find the smallest number from list [9,41,12,3,74,15]

smallest = None
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print('Smallest number is', smallest)   
    
