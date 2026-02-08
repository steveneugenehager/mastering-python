# example_basic_statistical_functions.py 
"""Experiment with the basic statistical functions."""
# v2 - Adding while loop so any number of integers can be input by the user.

import statistics

def main():

    numbers = []
    
    print("Enter as many integers as you want, one at at time (or 'q' to quit):")
    
    while True:
        user_input = input("Enter an integer: ")
        
        if user_input.lower() == 'q':
            break
        
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")
    
    numbers.sort()
    print("\n")
    print(f"You entered: {numbers}")
    print(f"The Minimum value is {min(numbers)}")
    print(f"The Maximum value is {max(numbers)}")
    print(f"The count of values is {len(numbers)}")
    print(f"The sum of values is {sum(numbers)}")
    print(f"The mean is {statistics.mean(numbers)}")      #  average/mean
    print(f"The median is {statistics.median(numbers)}")    #  middle value
    print(f"The mode is {statistics.mode(numbers)}")      #  most common value
    print(f"The standard deviation is {statistics.stdev(numbers)}")     #  standard deviation
    print(f"The variance is {statistics.variance(numbers)}")  

if __name__ == "__main__":
    main()
