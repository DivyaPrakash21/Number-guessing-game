import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Hello")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Ask the user to guess the number
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
number_guessing_game()
