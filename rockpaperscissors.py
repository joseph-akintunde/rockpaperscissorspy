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
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if userInput == 0:
  print(rock)
elif userInput == 1:
  print(paper)
else:
  print(scissors)
import random
computerChoice = random.randint(0,2)
if computerChoice == 0:
  print("Computer Chose: ")
  print(rock)
elif computerChoice == 1:
  print("Computer Chose: ")
  print(paper)
else:
  print("Computer Chose: ")
  print(scissors)
if userInput == 0 and computerChoice == 0 or userInput == 1 and computerChoice == 1 or userInput == 2 and computerChoice == 2:
  print("It is a draw")
elif userInput == 0 and computerChoice == 1:
  print("You lose")
elif userInput == 1 and computerChoice == 2:
  print("You lose")
elif userInput == 2 and computerChoice == 0:
  print("You lose")
else:
  print("You win. Congratulations!")
