player = input()
computer = {"rock", "paper", "scissors"}
choice_of_computer = list(computer)[0]
winner = ''-

if player == "rock":
    if choice_of_computer == "scissors":
        winner = "human"
    elif choice_of_computer == "rock":
        winner = "draw"
    elif choice_of_computer == "paper":
        winner = "computer"

if player == "scissors":
    if choice_of_computer == "scissors":
        winner = "draw"
    elif choice_of_computer == "rock":
        winner = "computer"
    elif choice_of_computer == "paper":
        winner = "human"

if player == "paper":
    if choice_of_computer == "scissors":
        winner = "computer"
    elif choice_of_computer == "rock":
        winner = "human"
    elif choice_of_computer == "paper":
        winner = "draw"

print(f'Player\'s choice: {player}\nComputer\'s choice: {choice_of_computer}\nWinner: {winner}')
