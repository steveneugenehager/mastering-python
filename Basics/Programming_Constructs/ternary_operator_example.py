# ternary_operator_example.py
"""Illustrate the ternary operator used in conditional assignment"""

def main():
    ages = [ 1, 17, 18, 65]
    for age in ages:
        status = ("adult" if age >= 18 else "child")
        print(f"{age=}; {status=} ")

if __name__ == "__main__":
    main()