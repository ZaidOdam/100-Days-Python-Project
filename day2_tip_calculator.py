print("Welcome to the tip calculator!")
bill=float(input("What was the total bill: "))
per=int(input("What percentage tip would you like to give? 10,12,15: "))
n=int(input("How many people to split the bill: "))
total=bill+per/100*bill #bill+(bill*per/100)
split=total/n
print("Each person should pay: {}/-".format(round(split,2)))

# num=input("Enter 2 digit Number: ")
# sum=0
# for i in range(len(num)):
#     sum+=int(num[i])
# print("Answer: {}".format(sum));

# BMI
# h=float(input("Enter your height in m "))
# w=int(input("Enter your weight in kg "))
# print(w//(h**2))

# age=int(input("Enter your Age: "))
# r=90-age
# day=r*365
# week=r*52
# mon=r*12
# print(f"you have {day} days, {week} weeks and {mon} months left")
