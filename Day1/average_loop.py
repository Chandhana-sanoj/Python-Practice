#average the numbers of list [9,41,12,3,74,15]

count=0
sum=0
print('before',count, sum)
for number in [9,41,12,3,74,15]:
     count = count + 1
     sum = sum + number
     print(count, sum, number)     
print('after',count,sum, sum/count)



#average only even numbers of list [9,41,12,3,74,15]
count=0
sum=0
print('before',count, sum)
for number in [9,41,12,3,74,15]:
    if number%2 == 0:
     count = count + 1
     sum = sum + number
     print(count, sum, number)     
print('after',count,sum, sum/count)
