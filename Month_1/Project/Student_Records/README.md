Build a menu-driven command-line program that stores student records in memory for one run. This guided project previews lists and dictionaries; Month 2 will explain those data structures in more depth.

## Learning goals

- Combine input, conversion, conditionals, loops, and functions.
- Keep validation and calculations in reusable functions.
- Test boundary cases and recover from expected invalid input.

## Features

1. Add a student with a unique ID, name, and three scores from 0 to 100.
2. View all students with their average and letter grade.
3. Find a student by ID and display an individual report.
4. Keep showing the menu until the user chooses to quit.
5. Reject blank names, duplicate IDs, non-numeric scores, and scores outside 0-100 without adding an invalid record.

Records are held in memory: they are lost when the program exits. File storage is outside this month's scope.

## Run

From this directory:

```bash
python student_management.py
```

Run the automated checks with:

```bash
python -m unittest -v
```

## Acceptance checklist

- [ ] Add two students and view both.
- [ ] Look up each student by ID and show the correct scores, average, and grade.
- [ ] A duplicate ID and blank name do not create a record.
- [ ] Test non-numeric, negative, and above-100 scores; the program retries safely.
- [ ] An unknown ID and unknown menu choice show helpful messages.
- [ ] Choosing quit exits cleanly.
- [ ] All automated tests pass.

## Extension ideas

- Add a fourth score and compute the average from all scores.
- Sort the student list by average.
- In Month 2, persist records to a file and load them on startup.
