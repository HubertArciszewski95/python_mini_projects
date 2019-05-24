# This file act as database
file_path = "/Users/hubertarciszewski/Downloads/users.txt"

# Save to list users from file
with open(file_path) as file:
    user_database = file.read().split()

while True:
    username = input("Enter your username: ").capitalize().strip()

    # Username validator logic
    valid_username = True

    if username == "":
        print("Username can't be empty")
        valid_username = False
    else:
        for x in user_database:
            if username == x:
                print("Username exits")
                valid_username = False

    # Add user to file
    if valid_username:
        with open(file_path, "a") as file:
            add_user = file.write(username + "\n")
        break


while True:
    password = input("Enter new password: ")

    length = False
    num = False
    upper = False

    # validator logic
    if len(password) >= 5:
        length = True
    for x in password:
        if x.isupper():
            upper = True
        elif x.isdigit():
            num = True

    if length and num and upper:
        print("Password is fine")
        break
    # validation messages
    else:
        print("Please check the followings:")
        if not length:
            print("You need at least 5 characters")
        if not num:
            print("You need at least one number")
        if not upper:
            print("You need at least one uppercase letter")

