# from random import randint
import random

choices = {
    "rock":"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper":"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

def rock_paper_scissors():  
    print("Welcome to Rock Paper Scissors!\n")
    player_choice = input("What do you choose? rock or paper or scissors:  ").lower()
    if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
        print(f"you chose {player_choice} ")
        print(choices[player_choice])
        computer_choice = random.choice(list(choices.values()))
        print("computer chose")
        print(computer_choice)

        if choices[player_choice] == choices["rock"] and computer_choice == choices["paper"]:
            print("You lost")
        elif choices[player_choice] == choices["rock"] and computer_choice == choices["scissors"]:
            print("You win")
        elif choices[player_choice] == choices["paper"] and computer_choice == choices["rock"]:
            print("You win")
        elif choices[player_choice] == choices["paper"] and computer_choice == choices["scissors"]:
            print("You lost")
        elif choices[player_choice] == choices["scissors"] and computer_choice == choices["rock"]:
            print("You lost")
        elif choices[player_choice] == choices["scissors"] and computer_choice == choices["paper"]:
            print("You win")
        else:
            print("It's a draw")

    else:
        print("please check your choice\n\n")
        rock_paper_scissors()
rock_paper_scissors()