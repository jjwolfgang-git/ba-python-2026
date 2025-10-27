import random, sys

wins=0
losses=0
ties=0

comp_moves = [ "ROCK", "PAPER", "SCISSORS" ]

print("ROCK, PAPERS, SCISSORS")

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    user_move = input(">")
    
    if (user_move == "r"):
        print("ROCK versus...")
    elif (user_move == "p"):
        print("PAPER versus...")
    elif (user_move == "s"):
        print("SCISSORS versus...")
    elif (user_move == "q"):
        sys.exit()
    else:
        print("Invalid move")
        continue
    
    cm = random.randint(0, 2)
    comp_move = comp_moves[cm]
    print(comp_move)
    
    if user_move == "r" and comp_move == "ROCK":
        print("It is a tie!")
        ties = ties + 1
    if user_move == "r" and comp_move == "PAPER":
        print("You lose!")
        losses = losses + 1
    if user_move == "r" and comp_move == "SCISSORS":    
        print("You win!")
        wins = wins + 1
        
    if user_move == "p" and comp_move == "ROCK":
        print("You win!")
        wins = wins + 1
    if user_move == "p" and comp_move == "PAPER":
        print("It is a tie!")
        ties = ties + 1
    if user_move == "p" and comp_move == "SCISSORS":    
        print("You lose!")
        losses = losses + 1
        
    if user_move == "s" and comp_move == "ROCK":
        print("You lose!")
        losses = losses + 1
    if user_move == "s" and comp_move == "PAPER":
        print("You win!")
        wins = wins + 1
    if user_move == "s" and comp_move == "SCISSORS":    
        print("It is a tie!")
        ties = ties + 1
