#   A Python dictionary uses the syntax of curly brackets enclosing the
# pairs of the structure separated by commas, with the key separated from the value with a colon.
#   A dictionary's values can contain differing data types and even complex items 
# like other objects. The dictionary's keys must be immutable.

import statistics
from typing import Dict, List

# demonstrate the variety possible in a dictionary.
GRADE_BOOK: Dict[str, List[int]] = {
    'Susan': [92,85,100],
    'Eduardo': [83,95,79],
    'Azizi': [91,89,82],
    'Pantipa': [97,91,92],
}

def main():
    """
    Calculate and display individual student and class averages.
    
    Processes grades from GRADE_BOOK dictionary, computing the mean
    for each student and the overall class average.
    """
    # Calculate all students' individual averages. 
    # To be used in the class average calculation.
    # The list comprehension was introduced to compact the code.
    student_averages = [
        calculate_student_average(student, grades)
        for student, grades in GRADE_BOOK.items()
    ]
    
    # Display class average
    print()  # Blank line for readability
    display_class_average(student_averages)

def calculate_student_average(student: str, grades: List[int|float]) -> float:
    """
    Calculate and display a student's average grade.
    
    Args:
        student: Student's name
        grades: List of integer/float grades
    
    Returns:
        The student's average grade
    """
    average = statistics.fmean(grades)
    print(f"{student:<20} average = {average:6.2f}")
    return average


def display_class_average(averages: List[float]) -> None:
    """
    Display the overall class average.
    
    Args:
        averages: List of student averages
    """
    # If there were students, show the class average.
    if averages:
        class_avg = statistics.fmean(averages)
        print(f"{'Class':<20} average = {class_avg:6.2f}")


if __name__ == "__main__":
    main()

