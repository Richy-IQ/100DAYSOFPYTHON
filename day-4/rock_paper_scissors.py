#!/usr/bin/python3

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

#Write your code below this line 👇

images = [rock, paper, scissor]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor "))
print(images[my_choice])

if my_choice >= 3 or my_choice < 0:
    print("It's an invalid number")
else:

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{images[computer_choice]}")
    if my_choice == 0 and computer_choice == 2:
        print("You Win")
    elif computer_choice > my_choice:
        print("You lose")
    elif computer_choice < my_choice:
        print("You win")
    elif my_choice == computer_choice:
        print("It's a draw")
