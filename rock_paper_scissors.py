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
game_images = [rock, paper, scissors]
user = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors. \n"))
if user >=3 or user < 0:
  print("you have enter a invalid choice!! You lose")
else:
  print(game_images[user])
  
  computer = random.randint(0,2)
  
  print("Computer choice: ")
  print(game_images[computer])
  
  if (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
      print("You won!!")
  elif (computer == 0 and user == 2) or (computer == 2 and user == 1) or (computer == 1 and user == 0):
      print("You lose")
  else:
      print("It's a draw")
