from random import randint

player_score = 0
computer_score = 0
round_count = 1
winning_score = 3

while True:
    print(f"ROUND {round_count} start")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("(enter your's choice): ").lower()
    if player == "quit" or player == "q":
        print("You quit the game")
        break

    # input validation
    while player != "rock" and player != "paper" and player != "scissors":
            print("Not valid choice \nTry Again!")
            player = input("(enter your's choice): ").lower()

    # computer logic
    computer = randint(1, 3)
    if computer == 1:
        computer = "rock"

    elif computer == 2:
        computer = "paper"

    else:
        computer = "scissors"
    print(f"COMPUTER pick: {computer}")

    print("\nSHOOT!\n")

    # game logic
    if player == "rock" and computer == "paper":
        print(f"computer win round {round_count}")
        computer_score += 1

    elif player == "paper" and computer == "rock":
        print(f"You win round {round_count}")
        player_score += 1

    elif player == "rock" and computer == "scissors":
        print(f"You win round {round_count}")
        player_score += 1

    elif player == "scissors" and computer == "rock":
        print(f"computer win round {round_count}")
        computer_score += 1

    elif player == "scissors" and computer == "paper":
        print(f"You win round {round_count}")
        player_score += 1

    elif player == "paper" and computer == "scissors":
        print(f"computer win round {round_count}")
        computer_score += 1

    else:
        print(f"Round {round_count} is a draft")

    # round counter
    round_count += 1

    # Showing score after each round
    print(f"The score is:\n{computer_score} for computer \n{player_score} for you\n")

    # scoring logic
    if computer_score == winning_score:
        print("COMPUTER WIN GAME")

    elif player_score == winning_score:
        print("YOU WIN GAME")

    # Play again logic
    if player_score == winning_score or computer_score == winning_score:
        play_again = input("Do you want play again? (y/n) ").lower()

        if play_again == "y":
            print("\nNew game start!\n")
            computer_score = 0
            player_score = 0
            round_count = 1
        else:
            print("Thank for playing. Bye Bye")
            break
