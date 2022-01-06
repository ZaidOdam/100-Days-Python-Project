import os
from caesar_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]  
    else:
      end_text+=char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

flag=True
while flag:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  temp=input("Type 'yes' if you want to go again, Otherwise type 'no': ")
  if temp=='no':
    flag=False
    print("GoodBye")
  else:
      os.system('cls')

# Step 1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# def encrypt(plain_text,shift_num):
#   res=""
#   for letter in plain_text:
#     idx=alphabet.index(letter)
#     res+=alphabet[(idx+shift_num)%26]
#   print(f"The encoded text is {res}")
# encrypt(text,shift)

#Step 2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n")
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
# def decrypt(cipher_text,shift_num):
#   plain_text=""
#   for letter in cipher_text:
#     idx=alphabet.index(letter)
#     if idx-shift_num<0:
#       idx+=26
#     plain_text+=alphabet[idx-shift_num]
#   print(f"The decoded text is {plain_text}"
# if direction=="encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction=="decode":
#   decrypt(text,shift)
# else:
#   print("Invalid")



# Exercise

# import math
# def paint_calc(height,width,cover):
#   area=height*width
#   ans=math.ceil(area/cover)
#   print(f"You will need {ans} cans of paint")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# def prime_checker(number):
#   flag=True

#   for i in range(2,number):
#     if number%i==0:
#       flag=False
#       print("It's not a prime number")
#       break
  
#   if flag==True:
#     print("It's a prime number")
# n = int(input("Check this number: "))
# prime_checker(number=n)