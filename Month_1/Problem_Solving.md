# Month 1 - A beginner's problem-solving method

Programming is more than remembering syntax. Use this repeatable method for the exercises and projects in this month.

## 1. Understand the task

Restate the goal in one sentence. List:

- **Inputs:** What information does the user or program provide?
- **Outputs:** What should the program display or return?
- **Rules:** What decisions or calculations connect the inputs to the outputs?
- **Constraints:** What values are invalid, missing, or at a boundary?

For example, a calculator needs two numbers and an operation, returns one result, and must reject an unknown operation and division by zero.

## 2. Work through a small example

Choose concrete values and calculate the expected result by hand. Include:

- A typical case
- A boundary case (such as zero)
- An invalid case (such as text where a number is required)

Writing down expected results before coding makes mistakes easier to notice.

## 3. Write the steps before the Python

Use plain language or pseudocode:

```text
ask for the first number
ask for the operation
ask for the second number
if the operation is division and the second number is zero:
    report that division by zero is not allowed
otherwise:
    calculate and display the result
```

Translate one step at a time into Python. Start with the simplest working case; add validation and extra features afterward.

## 4. Trace and test

Follow the values through the program in order. For each condition, ask whether it is true for the test input and which branch runs.

After the ordinary case works, test boundaries and invalid inputs. If the result is wrong, reduce the problem: check one input, expression, or branch at a time. Make a change, rerun the same test, and confirm the behavior.

## 5. Break a larger task into pieces

When a program has several responsibilities, name the smaller jobs first: read input, validate it, calculate a result, and display the result. Week 4 introduces functions for separating these jobs. Do not create a function just to wrap one obvious line; use one when it gives a meaningful name to a reusable task.

## Practice

Use this method with the [Calculator](./Project/Calculator/README.md), [Expense Tracker](./Project/Expense_Tracker/README.md), and [Student Management System](./Project/README.md). For each, write down at least three test cases before running your program.
