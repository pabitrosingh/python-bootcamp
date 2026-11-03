"""Generate a report card from three validated scores."""


def ask_for_score(score_number):
    while True:
        score_text = input(f"Enter score {score_number} (0-100): ")
        try:
            score = float(score_text)
        except ValueError:
            print("Please enter a number.")
            continue

        if 0 <= score <= 100:
            return score
        print("Score must be between 0 and 100.")


def calculate_average(scores):
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


def main():
    name = input("Student name: ").strip()
    scores = []
    for number in range(1, 4):
        scores.append(ask_for_score(number))
    average = calculate_average(scores)
    grade = letter_grade(average)

    print("\nStudent Report")
    print("--------------")
    print(f"Name: {name}")
    for number, score in enumerate(scores, start=1):
        print(f"Score {number}: {score:.1f}")
    print(f"Average: {average:.1f}")
    print(f"Letter grade: {grade}")


if __name__ == "__main__":
    main()
