import numpy as np

NUMBER_OF_TRIES = 10


def ask_for_guess():
    try:
        guess = int(input("Enter a number between 1 and 100:"))
    except ValueError:
        print("Your input must be a number! Try again")
        return ask_for_guess()

    if guess < 1 or guess > 100:
        print("Your input must be between 1 and 100! Try again")
        return ask_for_guess()

    return guess


def start_game():
    print("The machine will pick a number between 1 and 100")
    print("Try to guess what it picked!")

    machine_guess = int(np.random.random() * 100)

    guess_number = 0
    while guess_number < NUMBER_OF_TRIES:
        print(f"You have {NUMBER_OF_TRIES - guess_number} guesses")
        guess = ask_for_guess()

        if guess == machine_guess:
            print("You guessed correctly!")
            break
        elif guess < machine_guess:
            print("Not quite... your guess is below the real value")
        elif guess > machine_guess:
            print("Not quite... your guess is above the real value")

        guess_number += 1


if __name__ == "__main__":
    start_game()
