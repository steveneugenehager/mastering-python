# casino_game_simulation.py
"""
Docstring for Quests.Simpler_examples.casino_game_simulation

Introduction to a class definition.
Introduction to methods
"""

import random
from collections import Counter

ITERATIONS=1_000_000

class CrapsSimulator:
    def __init__(self, iterations: int = 100_000):
        self.iterations = iterations
        self.stats = Counter()

    def roll_dice(self) -> int:
        # simulates two dye being rolled. Adds the faces together (2, ..., 12).
        return sum(random.choices(range(1, 7), k=2))

    def play_round(self) -> str:
        # --- Phase 1: Come-Out Roll ---
        come_out = self.roll_dice()
        
        if come_out in {7, 11}:
            return "Win (Natural)"
        if come_out in {2, 3, 12}:
            return "Loss (Craps)"
        
        # --- Phase 2: The Point Phase ---
        point = come_out
        while True:
            next_roll = self.roll_dice()
            if next_roll == point:
                return "Win (Point Made)"
            if next_roll == 7:
                return "Loss (Seven-Out)"

    def run_simulation(self):
        for _ in range(self.iterations):
            result = self.play_round()
            self.stats[result] += 1

    def display_results(self):
        total_wins = self.stats["Win (Natural)"] + self.stats["Win (Point Made)"]
        total_losses = self.stats["Loss (Craps)"] + self.stats["Loss (Seven-Out)"]
        
        print(f"Simulation Results ({self.iterations:,} rounds):")
        print("-" * 45)
        for outcome, count in sorted(self.stats.items()):
            print(f"{outcome:<20} | {count:>10d} | {(count/self.iterations):>7.2%}")
        print("-" * 45)
        print(f"{'TOTAL WINS':<20} | {total_wins:>10d} | {(total_wins/self.iterations):>7.2%}")
        print(f"{'TOTAL LOSSES':<20} | {total_losses:>10d} | {(total_losses/self.iterations):>7.2%}")

if __name__ == "__main__":
    #Instantiate the class.
    sim = CrapsSimulator(ITERATIONS)
    #Play the game a number of times.
    sim.run_simulation()
    #Review the results.
    sim.display_results()