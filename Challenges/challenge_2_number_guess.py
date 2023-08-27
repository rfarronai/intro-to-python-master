"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    answer = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20")
    guess = int(input("Guess a number: "))

    for _ in range(3):



        if guess == answer:
            print(f"You win!")
            return
        if guess < answer:
            print(f"Guess higher")
        elif guess > answer:
            print(f"Guess lower")
        guess = int(input("Guess a number: "))

    print(f"Game over. The number is: {answer}")

run_game()