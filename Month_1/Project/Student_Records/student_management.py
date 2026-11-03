"""In-memory student management capstone for Month 1."""


def calculate_average(scores):
    if not scores:
        raise ValueError("At least one score is required.")
    return sum(scores) / len(scores)


def letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def add_student_record(students, student_id, name, scores):
    student_id = student_id.strip()
    name = name.strip()

    if not student_id:
        raise ValueError("Student ID cannot be blank.")
    if not name:
        raise ValueError("Student name cannot be blank.")
    if any(student["student_id"] == student_id for student in students):
        raise ValueError("That student ID already exists.")
    if len(scores) != 3:
        raise ValueError("A student must have exactly three scores.")
    if any(score < 0 or score > 100 for score in scores):
        raise ValueError("Each score must be between 0 and 100.")

    student = {
        "student_id": student_id,
        "name": name,
        "scores": list(scores),
    }
    students.append(student)
    return student


def read_score(score_number):
    while True:
        score_text = input(f"Score {score_number} (0-100): ")
        try:
            score = float(score_text)
        except ValueError:
            print("Please enter a number, such as 82 or 82.5.")
            continue

        if 0 <= score <= 100:
            return score
        print("Score must be between 0 and 100.")


def add_student(students):
    student_id = input("Student ID: ").strip()
    name = input("Student name: ").strip()
    scores = []
    for number in range(1, 4):
        scores.append(read_score(number))

    try:
        student = add_student_record(students, student_id, name, scores)
    except ValueError as error:
        print(f"Student not added: {error}")
        return

    print(f"Added {student['name']} (ID: {student['student_id']}).")


def print_student(student):
    average = calculate_average(student["scores"])
    print(f"ID: {student['student_id']} | Name: {student['name']}")
    print(f"Scores: {', '.join(f'{score:.1f}' for score in student['scores'])}")
    print(f"Average: {average:.1f} | Grade: {letter_grade(average)}")


def view_students(students):
    if not students:
        print("No students have been added.")
        return

    for student in students:
        print_student(student)
        print()


def find_student(students, student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def show_student_report(students):
    student_id = input("Student ID to find: ").strip()
    student = find_student(students, student_id)
    if student is None:
        print(f"No student found with ID {student_id}.")
        return
    print_student(student)


def main():
    students = []
    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. View all students")
        print("3. Find student report")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            show_student_report(students)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
