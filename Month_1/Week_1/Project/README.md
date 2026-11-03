# Mini project - Student Profile Generator

Create an interactive command-line program that gathers a student's basic profile and displays a neatly formatted summary.

## Requirements

Ask for:

- The student's name
- Their age in whole years
- Their favorite subject
- The number of study hours they want to complete this week

Display a short profile using readable labels and f-strings. Include the weekly study goal in hours. Remove extra spaces around text answers with `.strip()`.

## Steps

1. Create or open `student_profile_generator.py`.
2. Collect each answer with `input()`.
3. Convert age and study hours to integers.
4. Print the formatted profile.
5. Run it with valid sample answers and compare the output to your expectations.

## Acceptance checklist

- [ ] Prompts clearly tell the user what to enter.
- [ ] The numeric answers are converted before use.
- [ ] The output includes all four answers and is easy to read.
- [ ] Text with accidental leading/trailing spaces is displayed cleanly.

This first project assumes valid numeric input. You will learn to handle invalid input in Week 4.