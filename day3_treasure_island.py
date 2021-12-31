#3.1 Odd Even
# num=int(input("Enter Any Number: "))
# if num%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

# BMI 2.O
# h=float(input("Enter your height in m "))
# w=int(input("Enter your weight in kg "))
# bmi=w//(h**2)
# if bmi<18.5:
#     print("Underweight")
# elif bmi<25:
#     print("Normal weight")
# elif bmi<30:
#     print("over weight")
# elif bmi<35:
#     print("obese")
# else:
#     print("clinically obese")

# Leaf Year
# year=int(input("Enter any year: "))
# if year%4==0:
#     if year%100==0 and year%400==0:
#         print("it's leap year")
#     elif year%100!=0:
#         print("it's leap year")
#     else:
#         print("Not leap year")
# else:
#     print("Not leaf year")

# Pizza Order
# Total=0
# size=input("Size of Pizza? S, M, L ")
# add=input("Add Pepperoni? Y or N ")
# cheese=input("Add Cheese? Y or N ")
# if size=='S':
#     Total+=15
# elif size=='M':
#     Total+=20
# else:
#     Total+=25
# if add=='Y':
#     if size=='S':
#         Total+=2
#     else:
#         Total+=3
# if cheese=='Y':
#     Total+=1
# print(f"Your Final Bill is: ${Total}")

# Love Calculator
# name1=input("What is your name? ")
# name2=input("What is there name? ")
# name=name1+name2
# name.lower()
# d1=name.count("t")+name.count("r")+name.count("u")+name.count("e")
# d2=name.count("l")+name.count("o")+name.count("v")+name.count("e")
# ans=d1*10+d2
#
# if ans<10 or ans>90:
#     print(f"Your score is {ans}. you go together like coke and mentos ")
# elif ans>=40 and ans<=50:
#     print(f"your score is {ans}. you are alright together")
# else:
#     print("Your score is {}".format(ans))

# Treasure Island
print('''
        Treasure Island
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to treasure island")
dir=input("Left or Right? ").lower()
if dir=="left":
    action=input("Swim to Wait? ").lower()
    if action=="wait":
        door=input("Which door Red, Yellow or Blue ").lower()
        if door=="yellow":
            print("You found the treasure")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")




