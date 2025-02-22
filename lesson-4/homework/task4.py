import random

def play_game():
    while True:
        secret_number = random.randint(1, 100)
        attempts = 10

        print("\nI have selected a number between 1 and 100. Try to guess it!")

        for _ in range(attempts):
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("You guessed it right! 🎉")
                return  
        print("You lost. Want to play again? (Y/YES/y/yes/ok)")
        play_again = input().strip().lower()
        if play_again not in ('y', 'yes', 'ok'):
            print("Thanks for playing! Goodbye. 👋")
            break 


play_game()
