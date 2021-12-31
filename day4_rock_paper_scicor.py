# Seed headtail and randomselection
# import random
# test_seed=int(input("Enter a Seed number "))
# random.seed(test_seed)
# # ans=random.randint(0,1)
# # if ans==0:
# #     print("Heads")
# # else:
# #     print("Tails")
# str1=input("Enter everyone name followed by , ")
# list1=str1.split(", ")
# idx=random.randint(0, len(list1))
# print(f"Bill is gonna pay is {list1[idx]}")

# Pick
# row1=['😂','🤪','😜']
# row2=['😛','🤔','😍']
# row3=['😯','😁','🙂']
# map=[row1,row2,row3]
# print(row1,row2,row3,sep="\n")
# loc=input("Enter row and col number")
# print("Emoji: {}".format(map[int(loc[0])][int(loc[1])]))


#Rock paper scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand=[rock,paper,scissors]
num=int(input("Type 0 for Rock, 1 for paper or 2 for scissor\n"))
if num>3 or num<0:
    print("Invalid Selection")
else:
    print(hand[num])
rnd= random.randint(0,2)
print("Computer:")
print(hand[rnd])

if num>3 or num<0:
    print("Invalid Selection you lose")
elif num==rnd:
    print("Draw")
elif num==(rnd+1)%3:
    print("You Won")
else:
    print("You Lose")
