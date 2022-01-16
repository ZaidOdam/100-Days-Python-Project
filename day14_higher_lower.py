from compare_art import logo,vs
from compare_game_data import data
import os,random

game_on=True
score=0
print(logo)
B=random.choice(data)
while game_on:
    A=B
    B=random.choice(data)

    while A==B:
        B=random.choice(data)

    #Can make function to generate string
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    ans=input("Who has more followers? Type 'A' or 'B': ").upper()
    if A['follower_count']>B['follower_count']:
        max='A'
    else:
        max='B'
    
    os.system('cls')
    print(logo)
    #can make a function with take both followers and guess to reture True or False like
    # if A.follower>B.follower:
    #     return guess=='A'
    # else:
    #     return guess=='B'
    if ans==max:
        score+=1
        print(f"You're right! Current score {score}")
    else:
        game_on=False
        print(f"Sorry, that's wrong. Final score {score}")

