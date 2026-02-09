# dice_roll_simulation.py
"""
    Simple example using random library.
    Introduction to the Counter object.
    """
# v2 - randint is more succint than randrange for my need here.
#   A Final "Pro" Optimization
#       If you want to make this even faster, there is one more tool in the random module 
#           specifically designed for large simulations: random.choices().
#       Instead of a loop that calls a function 6 million times, random.choices() performs the 
#           heavy lifting in C-code and returns the entire collection at once.

import random
from collections import Counter

def main() -> None:
    """Entry point for the script logic."""
    iterations = 6 * 1_000_000 
    stats = Counter(random.randint(1,6) for i in range(iterations))
        
    # Printing sorted by key, right-justified
    print(f"{'Side':<5} | {'Count':>10}")
    print("-" * 18)
    # Sort by die_face and print frequency for the run.
    for die_face in sorted(stats):
        print(f"{die_face:<5} | {stats[die_face]:10d}")

if __name__ == "__main__":
    main()