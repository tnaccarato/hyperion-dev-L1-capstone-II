# ------------------------------------------------------------------------------
# Author: Tom Naccarato (tcarlnaccarato@gmail.com)
#
# task_manager.py (c) 2022
#
# Description:  A program for a small business to assign and manage tasks for
#               members of a team.
#
# Created:  2022-05-31T19:04:46.664Z
#
# Modified: 2022-06-01T00:12:37.118Z
# ------------------------------------------------------------------------------
# Imported Libraries
from datetime import date
# ------------------------------------------------------------------------------

# ====Login Section====

# Creates an empty lists for the user.txt details
usernames = []
passwords = []
# Opens and reads user.txt and adds each username and password to above lists
with open("user.txt", "r") as user:
    for line in user:
        line = line.replace("\n", "")
        users_list = line.split(", ")
        usernames.append(users_list[0])
        passwords.append(users_list[1])
# Prompts user for username and checks if it is in the users.txt
username_attempt = input("Please enter your username:\n")
while username_attempt not in usernames:
    username_attempt = input("Username not recognised. Please try again.\n")
# Gets the index of the correct username for checking against password (1)
username_index = usernames.index(username_attempt)
# Asks user for password and checks it against the corresponding username index
password_attempt = input("Please enter your password:\n")
while password_attempt != passwords[username_index]:
    password_attempt = input("Incorrect password. Please try again.\n")


# ====Menu Selection====

while True:
    print("Select one of the following options below:")
    # If the user is admin, displays an additional option in the menu
    if username_attempt == "admin":
        print("\
    ds - Display statistics")
    # Displays the regular menu for users, making sure their input is lowercase
    # and stripping whitespace
    menu = input('''\
    r -  Register a new user
    a -  Add a task
    va - View all tasks
    vm - View my tasks
    e -  Exit
    : ''').lower().strip(" ")

    # Registers a new user
    if menu == 'r':
        # Checks that user is admin
        if username_attempt == "admin":
            # Asks user for a new username and password
            new_username = input("Please enter a new username:\n")
            new_password = input("Please enter a new password for this user:\
\n")
            confirm_password = input("Please confirm your password:\n")
            # Checks password against repeated password to check they
            # are the same
            while new_password != confirm_password:
                new_password = input("Passwords were not the same. Please \
enter your new password again.\n")
                confirm_password = input("Please confirm your password:\n")
            # When the passwords match, writes new user details
            # to user.txt (2)
            with open("user.txt", "a") as user:
                user.write(f"\n{new_username}, {new_password}")
        # If user is not admin, prints an error message
        else:
            print("Sorry, only the admin can register a new user.")

    # Adds a task to tasks.txt
    elif menu == 'a':
        # Prompts user for task data
        user_assigned = input("Who is this task assigned to?\n")
        # Checks that user is in user.txt
        while user_assigned not in usernames:
            user_assigned = input("Username not recognised. Please try \
again.\n")
        task_title = input("What is the title of this task?\n")
        task_description = input("Please enter a description for this task:\n")
        due_date = input("When is this task due?\n")
        # Gets current date (3)
        today_date = date.today().strftime("%d %B %Y")
        complete = "No"
        # Writes the task info to tasks.txt
        with open("tasks.txt", "a") as tasks:
            tasks.write(f"\n{user_assigned}, {task_title}, \
{task_description}, {due_date}, {today_date}, {complete}")

    # Reads tasks.txt and outputs them in a user friendly manner
    elif menu == 'va':
        # Opens and reads tasks.txt
        with open("tasks.txt", "r") as tasks:
            for line in tasks:
                line = line.split(", ")
                print(f'''
--------------------------------------------------------------------------------
Task:               {line[1]}
Assigned to:        {line[0]}
Date assigned:      {line[4]}
Due date:           {line[3]}
Task complete?      {line[5]}
Task description:
{line[2]}
--------------------------------------------------------------------------------
''')

    # Only prints tasks if username is the same as the team member
    # assigned
    elif menu == 'vm':

        with open("tasks.txt", "r") as tasks:
            for line in tasks:
                line = line.split(", ")
                if line[0] == username_attempt:
                    print(f'''
--------------------------------------------------------------------------------
Task:               {line[1]}
Assigned to:        {line[0]}
Date assigned:      {line[4]}
Due date:           {line[3]}
Task complete?      {line[5]}
Task description:
{line[2]}
--------------------------------------------------------------------------------
''')

    # Exits the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Displays statistics
    elif menu == 'ds':
        # Checks that user is admin
        if username_attempt == "admin":
            # Creates empty string for users and tasks
            user_str = ""
            tasks_str = ""
            # Reads and stores user.txt to user_str
            with open("user.txt", "r") as users:
                for line in users:
                    user_str += line
            # Splits user_str into lines to count
            lines_user = user_str.split("\n")
            # Reads and stores tasks.txt to tasks_str
            with open("tasks.txt", "r") as tasks:
                for line in tasks:
                    tasks_str += line
            # Splits tasks_str into lines to count
            lines_tasks = tasks_str.split("\n")
            # Prints the total number of users and tasks assigned
            print(f"There are currently {len(lines_user)} users and \
{len(lines_tasks)} tasks assigned.")
        # If user is not admin, prints an error message
        else:
            print("Nice try finding this option but only the admin can display\
 statistics!")

    # If the user does not enter one of the options, displays an error message
    else:
        print("You have made a wrong choice, please try again.")


# ------------------------------------------------------------------------------
# References
# ------------------------------------------------------------------------------
# (1) Used info from here for use of the index function:
# https://www.programiz.com/python-programming/methods/list/index

# (2) Used info from here from appending to the end of a text file:
# https://docs.python.org/3/library/functions.html#open

# (3) Used info from here for use of the datetime module:
# https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
# ------------------------------------------------------------------------------
