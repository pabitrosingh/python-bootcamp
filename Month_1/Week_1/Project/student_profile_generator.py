"""Collect and display a student's basic study profile."""


def main():
    name = input("Student name: ").strip()
    age = int(input("Age in years: "))
    favorite_subject = input("Favorite subject: ").strip()
    weekly_study_hours = int(input("Study goal for this week (hours): "))

    print("\nStudent Profile")
    print("---------------")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Favorite subject: {favorite_subject}")
    print(f"Weekly study goal: {weekly_study_hours} hours")


if __name__ == "__main__":
    main()