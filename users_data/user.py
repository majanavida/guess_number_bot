from random import randint


# Keep users, who started using bot 
users = {}


# Number of attempts per game
ATTEMPTS = 5


# Function, that guesses the number for the game 
def get_random_number() -> int:
    return randint(1, 100)