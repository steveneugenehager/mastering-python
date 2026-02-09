#verbose_variance.py
# Recreating the statistics.pvariance which calculates Population Variance
# Opportunity to usea list comprehension.

import statistics as s

DATA = (1,3,4,2,6,5,3,4,5,2)

def main() -> None:
    """Main entry point of the script."""
    population_variance =  determine_variance(*DATA)
    print('variance =' , population_variance)
    print('standard deviation =' , population_variance ** 0.5)


def determine_variance(*args) -> float:
    average = s.mean(args)
    # List comprehension eliminates 3 lines including a loop
    distances_squared = [(n - average)**2 for n in args]
    return(s.mean(distances_squared))


if __name__ == "__main__":
    main()