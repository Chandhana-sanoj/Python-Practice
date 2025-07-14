# Search for 12 in the list [9, 41, 12, 3, 74, 15] using a boolean flag

found=False
for value in [9,41,12,3,74,15]:
    if value == 12:
        found = True
        break
print(found,value)
