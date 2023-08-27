"""
Randomly returns two numbers between 1 and 6
"""

# Generate two random integer between 1 and 6 (inclusive)

# Tell the user what the result was

import random


def roll_dice(player_num):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print(f"Player {player_num} rolled {die1} and {die2} (total {die1 + die2})")


roll_dice(1)
roll_dice(2)
