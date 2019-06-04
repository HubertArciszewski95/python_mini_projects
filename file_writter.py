# List for words typed by user
words = []

while True:
    user_input = input("Write a value: ")

    # When user type "SAVE" then all words from list "words" will be added to file.
    # Loop continue to run and list "words" are cleared.
    if user_input == "SAVE":
        with open("user_data.txt", "a")as file:
            for x in words:
                file.write(x + "\n")

        words.clear()

    # When user type "CLOSE" then all words in list "words" are added to file.
    # Then loop break
    elif user_input == "CLOSE":
        with open("user_data.txt", "a") as file:
            for x in words:
                file.write(x + "\n")
        break

    # If user don't type "SAVE" or "CLOSE" then word is append to list "words"
    else:
        words.append(user_input)



