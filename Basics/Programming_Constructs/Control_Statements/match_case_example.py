# match_case_example.py
"""Simple match case example."""
# Used main boilerplate, type hints, docstrings, return, and match.

def main():
    print("Grade Translator")
    
    try:
        grade = float(input("Enter numeric grade (0-100): "))
        
        if 0 <= grade <= 100:
            letter = get_letter_grade(grade)
            print(f"Grade {grade} = {letter}")
        else:
            print("Please enter a grade between 0 and 100")
            
    except ValueError:
        print("Invalid input. Please enter a number.")

def get_letter_grade(score: int | float) -> str:
    """Convert a numeric grade to a letter grade.
    
    Args:
        score: Numeric grade from 0-100
        
    Returns:
        Letter grade (A+, A, A-, ..., or F)
    """
    match score:
        case score if score >= 97:
            return 'A+'
        case score if score >= 93:
            return 'A'
        case score if score >= 90:
            return 'A-'
        case score if score >= 87:
            return 'B+'
        case score if score >= 83:
            return 'B'
        case score if score >= 80:
            return 'B-'
        case score if score >= 77:
            return 'C+'
        case score if score >= 73:
            return 'C'
        case score if score >= 70:
            return 'C-'
        case score if score >= 67:
            return 'D+'
        case score if score >= 63:
            return 'D'
        case score if score >= 60:
            return 'D-'
        case score if score >= 0:
            return 'F'
        case _:
            return 'Invalid'

if __name__ == "__main__":
    main()