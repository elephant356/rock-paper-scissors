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

handSign = input("Rock, Paper, or Scissors? ").lower()
import random
hands = [rock, paper, scissors]
computersHand = random.choice(hands)

if handSign == "rock":
  print(f"You chose: {rock}")
  print(f"The Computer chose: {computersHand}")
 
  if computersHand == paper or computersHand == scissors:
    print("You Win! Rock beats everything except for Rock!")
  else:
    print("It's a draw! Try Again!")
  
if handSign == "paper":
  print(f"You chose: {paper}")
  print(f"The Computer chose: {computersHand}")
  if computersHand == rock:
    print("You Win! Paper beats rock!")
  elif computersHand == scissors:
    print(f"You Lose! Scissors beats Paper!")
  else:
    print("It's a draw! Try Again!")

if handSign == "scissors":
  print(f"You chose: {scissors}")
  print(f"The Computer chose: {computersHand}")
  if computersHand == rock:
    print("You Lose! Rock beats scissors!")
  elif computersHand == paper:
    print(f"You Win! Scissors beats Paper!")
  else:
    print("It's a draw! Try Again!")

elif handSign != "rock" and handSign != "paper" and handSign != "scissors":
  print("Invalid selection! Please type rock, paper or scissors!")
