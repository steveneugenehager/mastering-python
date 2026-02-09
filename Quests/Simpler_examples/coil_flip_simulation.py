# coil_flip_simulation.py
"""
    Simple example using random library.
    Introduction to the Counter object.
    Introduction to random.choices()
    """

import random
from collections import Counter

ITERATIONS = 2 * 1_000_000
OUTCOMES = ["Heads", "Tails"]

def main() -> None:
    """Entry point for the script logic."""
    stats = Counter(random.choices(OUTCOMES, k=ITERATIONS))
        
    # Printing sorted by key, right-justified
    print(f"{'Side':<5} | {'Count':>10}")
    print("-" * 18)
    # Sort by outcome and print frequency for the run.
    for outcome, count in sorted(stats.items()):
        print(f"{outcome:<5} | {count:10d}")

if __name__ == "__main__":
    main()