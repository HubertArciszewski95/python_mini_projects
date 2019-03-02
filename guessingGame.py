from random import randint

random_number = (randint(1, 10))

while True:
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess == random_number:
        print("You guess it, You won!")
        play_again = input("Do you want play again? (y/n) ").lower()

        if play_again == "y":
            random_number = randint(1, 10)
        else:
            print("Thank for playing. Bye Bye")
            break

    elif user_guess > random_number:
        print("To high, Try again")

    elif user_guess < random_number:
        print("To low, Try again!")

