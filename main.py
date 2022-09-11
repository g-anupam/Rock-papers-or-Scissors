import random

def user():
    a = input("Rock papers or Scissors?")
    return a

def computer():
    b = random.choice(["rock","paper","scissors"])
    return b

def flow():
    a = input("Would you like to continue?[Y/N]")
    if a in "yY":
        evaluate()
    elif a in "nN":
        print("Game over")
    else:
        print("Invalid entry")
        flow()




def evaluate():
    x = user()
    y = computer()
    print("The computer chose:",y)
    if x == "rock" and y == 'paper':
        print("You Lose!")
        flow()
    elif x == "rock" and y == "scissors":
        print("You Win!")
        flow()
    elif x == "rock" and y == "rock":
        print("Its a draw!")
        flow()
    elif x == "paper" and y == "paper":
        print("Its a draw!")
        flow()
    elif x == "paper" and y == "rock":
        print("You Win!")
        flow()
    elif x == "paper" and y == "scissors":
        print("You Lose!")
        flow()
    elif x == "scissors" and y == "scissors":
        print("Its a draw!")
        flow()
    elif x == "scissors" and y == "paper":
        print("You Win!")
        flow()
    elif x == "scissors" and y == "rock":
        print("You Lose!")
        flow()
    else:
        print("Invalid input")
        flow()

evaluate()
