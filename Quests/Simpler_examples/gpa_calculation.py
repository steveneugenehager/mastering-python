# gpa_calculation.py
"""Take a list of letter grades from the user and calculate the numeric GPA"""
# illustrate split and match/case
# Too simple of an approach - doesn't weight the GPA by credit hours per grade.

import statistics

GRADE_VALUES = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'D-': 0.7,
    'F': 0.0
}

def main():
    grades_input = input("Enter letter grades separated by spaces (e.g., A B C D F): ")
    grades_list = grades_input.upper().split()
    
    print(f"\nYou entered {len(grades_list)} grades:")
    print(grades_list)

    numeric_grades = []

    grades_list.sort()
    # Check validity
    for grade in grades_list:
        if grade in GRADE_VALUES:
            numeric_grades.append( GRADE_VALUES[grade] )
        else:
            print(f"WARNING: Invalid data - input = '{grade}'")
        
    if numeric_grades:
        print(f"{len(numeric_grades)} valid grades ({numeric_grades}) were detected.")
        print(f"The GPA is {statistics.mean(numeric_grades)}")

if __name__ == "__main__":
    main()