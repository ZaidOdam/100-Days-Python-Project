import os
from calculator_art import logo
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operator={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(logo)
    num1=float(input("What's the first number?: "))
    for key in operator:
        print(key)
    flag=True

    while flag:
        choice=input("pick an operation: ")
        function=operator[choice]
        num2=float(input("What's the next number?: "))
        answer=function(num1,num2)
        print(f"{num1} {choice} {num2} = {answer}")
        choice2=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'exit' to Exit: ").lower()
        if choice2=='y':
            num1=answer
        elif choice2=="n":
            flag=False
            os.system('cls')
            calculator()
        else:
            flag=False

calculator()


# Exercise

# def format_name(f_name,l_name):
#     name=f_name+" "+l_name
#     name=name.title()
#     # print(name)
#     return name
# print(format_name("zAiD","oDaM"))


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   day=month_days[month-1]
#   if is_leap(year) and month==1:
#     day+=1
#   return day

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
    
