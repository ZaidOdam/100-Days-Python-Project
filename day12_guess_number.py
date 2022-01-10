from random import randint
logo="""

 _____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                            
"""

print(logo)
print("Welcome to thee Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy or 'hard': ").lower()
if level=='hard':
    attempt=5
else:
    attempt=10

number=randint(1,100)
while attempt!=0:
    print(f"you have {attempt} remaining to guess the number.")
    choice=int(input("Make a guess: "))
    if choice==number:
        print(f"You got it! The answer was {number}")
        break
    elif choice>number:
        print("Too high")
    else:
        print("Too low")
    attempt-=1
    if attempt==0:
        print("You have run out of guesses, you LOSE!")
        break 
    else:
        print("Guess Again.")
  