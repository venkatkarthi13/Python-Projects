from guess_number import Guess
from r_p_s import RPS
import sys

def play_game(name='player'):
    welcomeBack=False
    
    while True:
        if welcomeBack == True:
            print(f"{name}, Welcome back to arcade menu")
            
        playerChoose=input(f"\n Chooose a game....\n 1 for Rock, Paper, Scissor\n 2 for Guess_number\n or x to exit\n")
        
        if playerChoose not in ["1","2","x"]:
            print(f"please choose a number between 1, 2 or x")
            return play_game(name)
        
        welcomeBack=True
        
        if playerChoose == "1":
            rps=RPS(name)
            return rps
        elif playerChoose == "2":
            guess_number=Guess(name)
            return guess_number
        else:
            print(f"\n{name} See you next time, Bye!")
            sys.exit()
            
if __name__=="__main__":
    import argparse
    parse=argparse.ArgumentParser(description="Welcome to Arcade") 
    parse.add_argument(
        "--name",metavar="name",required=True, help="Name of the person who play's" 
    )
    args=parse.parse_args()
    print(f"Hi {args.name}, Welcome to the Arcade☣️")
    arcade=play_game(args.name)
  