#count the numbers of list [9,41,12,3,74,15]
count=0
print('before',count)
for number in [9,41,12,3,74,15]:
    count = count + 1  
    print(count,number) 
print('after',count)



#count the even numbers of list [9,41,12,3,74,15]
count=0
for number in [9,41,12,3,74,15]:
    if number%2 == 0:
     count = count + 1  
    print(count,number) 
