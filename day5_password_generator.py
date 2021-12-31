# Height Average
# import math
# import Integer as Integer
# student=input("Input list of student height: ").split()
# for i in range(0,len(student)):
#     student[i]=int(student[i])
# print(student)
# count=0
# sum=0
# max=Integer.MIN_VALUE
# max=-1
# for i in student:
#     if i>max:
#         max=i
#     count+=1
#     sum+=i
# ans=sum/count
# print("Average is {}".format(ans))
# print("Max height is {}".format(max))
# ans1=math.fsum(student)/float(len(student))
# print("Average is {}".format(ans1))

# Sum of even number
# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print("Sum of Even number {}".format(sum))
# or
# sum2=0
# for i in range(2,101,2):
#     sum2+=i
# print("Sum: {}".format(sum2))

# Fizz Buzz
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

import random
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['*','+','$','(',')','@','^','#']
letter=int(input("How many letter would you like? "))
num=int(input("How many number would you like? "))
sym=int(input("How many Symbol would you like? "))
ans=[]
for i in range(0,letter):
    ans.append(random.choice(alpha))

for i in range(0,num):
    ans.append(random.choice(number))

for i in range(0,sym):
    ans.append(random.choice(symbol))

random.shuffle(ans)
res=""
for i in ans:
    res+=i

print(res)