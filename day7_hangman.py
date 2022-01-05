import random
import os
from hangman_art import logo,stages
from hangman_words import word_list
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6
print(logo)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    print(logo)
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:  
        print(f"{guess} is not there you lose a life")
        lives-=1
        if lives==0:
            end_of_game="True"
            print("You lose")
        
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
   

# Excercise

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word=random.choice(word_list)
# guess=input("guess a letter: ").lower()
# for i in chosen_word:
#   if i==guess:
#     print("Right")
#   else:
#     print("Wrong")

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print(f'Pssst, the solution is {chosen_word}.')
# display=[]
# for i in range(len(chosen_word)):
#   display.append('_')
# print(display)
# guess = input("Guess a letter: ").lower()
# for i in range(len(chosen_word)):
#     if guess==chosen_word[i]:
#       display[i]=guess
# print(display)

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# print(f'Pssst, the solution is {chosen_word}.')
# display = []
# for _ in range(word_length):
#     display += "_"
# while '_' in display:
#   guess = input("Guess a letter: ").lower()
#   for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter
#   print(display)
# print("You won")

# import random
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# lives=6
# print(f'Pssst, the solution is {chosen_word}.')
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     temp=False
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter

#     if guess not in chosen_word:
#       lives-=1
#       if lives==0:
#         end_of_game="True"
#         print("You lose")
        
#     print(f"{' '.join(display)}")
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#     print(stages[lives])