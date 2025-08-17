"""Student Grade Manager.

This script allows adding student grades, calculating averages,
finding the topper, and printing a grade report.
"""

from typing import List, Dict


def calculate_average(grades: List[int]) -> float:
    """Calculate the average grade of a student.

    Args:
        grades (List[int]): A list of integer grades.

    Returns:
        float: The average of the grades.
    """
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def find_topper(students: Dict[str, List[int]]) -> str:
    """Find the student with the highest average grade.

    Args:
        students (Dict[str, List[int]]): Dictionary of student names to grades.

    Returns:
        str: The name of the student with the highest average.
    """
    topper = ""
    highest_avg = -1.0
    for name, grades in students.items():
        avg = calculate_average(grades)
        if avg > highest_avg:
            highest_avg = avg
            topper = name
    return topper


def main() -> None:
    """Main function to run the grade manager demo."""
    students = {
        "Alice": [85, 90, 88],
        "Bob": [70, 75, 72],
        "Charlie": [95, 92, 98],
        "David": [60, 65, 58],
    }

    for name, grades in students.items():
        avg = calculate_average(grades)
        print(f"{name}'s average grade: {avg:.2f}")

    topper = find_topper(students)
    print(f"\nTopper of the class is: {topper}")


if __name__ == "__main__":
    main()
