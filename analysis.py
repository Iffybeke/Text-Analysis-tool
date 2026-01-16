# Welcome user
def welcome_user():
    print("Welcome to Text-Analysis-tool. I will mine and analyze text data for insights.")

#Get Username
def get_username():
    #Print Message prompting for username
    usernameFrominput= input(f"\nTo begin, please enter your username:\n")
    return usernameFrominput

# Greet user
def greet_user(name):
    print(f"\nHello, {name}! Let's get started with your text analysis.")

welcome_user()
username = get_username()
greet_user(username)