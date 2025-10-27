import random, sys

wins=0
losses=0
ties=0

comp_moves = [ "r", "p", "s" ]
comp_names = [ "ROCK", "PAPER", "SCISSORS" ]

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
    comp_name = comp_names[cm]
    comp_move = comp_moves[cm]
    print(comp_name)
    
    if user_move == comp_move:
        print("It is a tie!")
        ties = ties + 1
    
    elif user_move == "r":
        if comp_move == "p":
            print("You lose!")
            losses = losses + 1
        if comp_move == "s":    
            print("You win!")
            wins = wins + 1
    elif user_move == "p":
        if comp_move == "r":
            print("You win!")
            wins = wins + 1
        if comp_move == "s":    
            print("You lose!")
            losses = losses + 1
        
    elif user_move == "s":
        if comp_move == "r":
            print("You lose!")
            losses = losses + 1
        if comp_move == "p":
            print("You win!")
            wins = wins + 1
