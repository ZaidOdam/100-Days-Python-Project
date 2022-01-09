import os
import random
from blackjack_art import logo

def card(score,flag):
    # flag: True for user
    #flag: False for computer
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    pick=int(random.choice(cards))
    
    if pick==11:
        if score+pick>21:
            pick=1
        else:
            if flag==True:
                choice=input("You got Ace card, select 1 or 11: ")
                if choice=="1":
                    pick=1
    return pick

def score(cards):
    # score=0
    # for i in cards:
    #     score+=i
    # return score
    return sum(cards)

def game_start():
    your_card=[]
    computer_card=[]
    for i in range (2):
        your_card.append(card(0,False))
        computer_card.append(card(0,False))

    flag=True
    while flag:
        your_score=score(your_card)
        computer_score=score(computer_card)
        print(f"Your cards: {your_card}, current score: {your_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if your_score>=21 or computer_score==21:
            break
        get_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if get_card=='n':
            flag=False
        else:
            your_card.append(card(your_score,True))

    while computer_score<16:
        computer_card.append(card(computer_score,False))
        computer_score=score(computer_card)



    print(f"\nYour Final hand: {your_card}, Final score: {your_score}")
    print(f"Computer final hand: {computer_card}, Final score: {computer_score}")

    if your_score==computer_score:
        print("Draw")
    elif your_score==21 and len(your_card)==2:
        print("BLACKJACK, YOU WON ")
    elif computer_score==21 and len(computer_score)==2:
        print("YOU LOSE, Computer has BLACKJACK")
    elif your_score>21:
        print("You went over, YOU LOSE")
    elif computer_score>21:
        print("Computer went over, YOU WON")
    elif computer_score<your_score:
        print("YOU WON")
    else:
        print("YOU LOSE")


intial=input("Do you want to play game of Blackjack? Type 'y' or 'n': ").lower()
if intial=='y':
    game_on=True
else:
    game_on=False

while game_on:
    print(logo)
    game_start()
    choice=input("Do you want to play game of Blackjack? Type 'y' or 'n': ").lower()
    if choice=='n':
        game_on=False
    else:
        os.system('cls')