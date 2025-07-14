#sum the numbers of list [9,41,12,3,74,15]
sum=0
print('before', sum)
for number in [9,41,12,3,74,15]:
     sum = sum + number 
     print(sum,number) 
print('after', sum)



#sum the even numbers of list [9,41,12,3,74,15]
sum=0
print('before', sum)
for number in [9,41,12,3,74,15]:
    if number%2 == 0:
     sum = sum + number 
     print(sum,number) 
print('after', sum)
