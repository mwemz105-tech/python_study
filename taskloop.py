# Task 1: numbers 1 to 50 in a list
num=list(range(1,51))
print(num)
# Task 2: numbers from task 1 divisible by 5 or 7
divisible=[]
for i in num:
    if i%7==0 or i%5==0:
        print(i)
        divisible.append(i)
print(divisible)

# Task 3: sum and average of numbers from 10 to 40
total=0

my_list=list(range(10,41))
for i in my_list:
    total=total+i
print(total)
average=total/len(my_list)
print(average)

# Task 3
num1=list(range(10,51))
odd=[]
count=0
for i in num1:
    if i%2!=0:
        odd.append(i)
        count=count+1
        if  count==10:
            break
print(odd)
