# Mini project - Student Report Card Generator

Build a command-line report card using small, reusable functions.

The program stores its three scores in a list. Treat this as a guided preview; lists are taught in Month 2.

## Requirements

- Ask for a student's name and three numeric scores.
- Each score must be from 0 to 100; non-numeric and out-of-range values should be retried with a helpful message.
- Calculate the average in its own function.
- Convert the average to a letter grade using A = 90-100, B = 80-89, C = 70-79, D = 60-69, F = below 60.
- Display the name, each score, average to one decimal place, and letter grade.
- Keep input, calculation, and display in separate functions.

## Acceptance checklist

- [ ] A non-numeric score does not crash the program.
- [ ] Scores below 0 or above 100 are rejected.
- [ ] Boundary averages 90, 80, 70, 60, and 59 receive the correct grades.
- [ ] Calculation functions return values rather than printing intermediate results.
