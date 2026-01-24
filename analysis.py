from random_username.generate import generate_username

# Welcome user
def welcome_user():
    print("Welcome to Text-Analysis-tool. I will mine and analyze text data.")

# Get Username
def get_username():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        if attempts == 0:
            inputPrompt = "\nTo begin, please enter your username:\n"
        else:
            inputPrompt = "\nPlease try again:\n"

        usernameFromInput = input(inputPrompt).strip()

        if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
            print(
                "Your username must be at least 5 characters long "
                "and contain only letters, numbers, or underscores."
            )
            attempts += 1
        else:
            return usernameFromInput

    print(f"\nMaximum {max_attempts} attempts reached. Assigning a random username.")
    return generate_username()

# Greet user
def greetuser(name):
    print(f"\nHello, {name}! Let's get started with your text analysis.")

# Program execution
welcome_user()
username = get_username()
greetuser(username)
