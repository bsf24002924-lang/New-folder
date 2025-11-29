print("Welcome to Paper, Scissor, Rock Game:)")
import random

user_wins=0
computer_wins=0
Draw=0

options=["paper","scissor","rock"]
while True:
    user_input=input("Enter Paper/Scissor/Rock or Q to quit: ").lower()
    if(user_input=="q"):
        break
    if(user_input not in options):
       print("Invalid input!<Try Again>")
       continue

    _input=random.randint(0,2)
    computer_input=options[_input]
    print("Computer chooses",computer_input,".")

    if(user_input == computer_input):
        print("Game Draw")
        Draw+=1

    elif(user_input =="rock" and computer_input== "scissor"):
        print("You win")
        user_wins+=1
    elif(user_input =="paper" and computer_input== "rock"):
        print("You win")
        user_wins+=1
    elif(user_input =="scissor" and computer_input== "paper"):
        print("You win")
        user_wins+=1
    else:
        print("Computer wins")
        computer_wins+=1


print(f"Game Draws {Draw} times")
print(f"You win {user_wins} times")
print(f"Computer wins {computer_wins} times")




