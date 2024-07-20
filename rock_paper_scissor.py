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
choices = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = choice = int(input())
random_choice = random.randint(0,2)
print(choices[choice])
print(choices[random_choice])

if choice - random_choice == 0:
  print("It's a draw! Try again.")
elif choice - random_choice == -1 or choice - random_choice == 2:
  print("You lost!")
elif choice - random_choice == 1 or hoice - random_choice == -2:
  print("You win! Congrats!")

print("Press 'Enter' to exit.")
input()