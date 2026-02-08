# walrus_operator_example.py
"""Example using the walrus operator in a control (while) statement."""
# Used a function to massage two different user-supplied values.

def main():

    base = get_valid_number("Enter the base: ", float)
    power = 0
    limit = get_valid_number("Enter the limit: ", float)

    while (answer := base ** power) <= limit:
        print(f"testing {base} raised to the {power} power. {answer=}")
        power += 1 
    else:
        print(f"INFO: while loop ended. {base=} {power=} {limit=} {answer=}")
	

def get_valid_number(prompt: str, num_type=float, min_val=None, max_val=None):
    """Get a valid number from user with optional range validation."""
    while True:
        try:
            number = num_type(input(prompt))
            
            # Check min/max if specified
            if min_val is not None and number < min_val:
                print(f"Number must be at least {min_val}")
                continue
            if max_val is not None and number > max_val:
                print(f"Number must be at most {max_val}")
                continue
            
            return number
            
        except ValueError:
            print(f"Invalid input. Please enter a valid {num_type.__name__}.")


if __name__ == "__main__":
    main()