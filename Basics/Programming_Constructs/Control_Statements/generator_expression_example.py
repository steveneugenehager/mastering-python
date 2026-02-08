# generator_expression_example.py
"""Demonstrate a generator expression - Generate a sum of squares """

def main():
    while True:
        try:
            number = int(input("Enter the number of square to sum (as an integer): "))
            break  # Valid input, exit loop
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"You entered a count of: {number}")

    # Here is the generator expression.
    print(f"The sum of squares for 1 to {number} is: {sum( x ** 2 for x in range(1, number + 1) )}")

if __name__ == "__main__":
    main()