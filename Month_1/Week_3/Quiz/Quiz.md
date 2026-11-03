# Week 3 quiz - Loops

Try each question before checking [Answers.md](./Answers.md).

1. What values are produced by `range(2, 7)`?
2. Does `range(5)` include 5?
3. When is a `for` loop a natural choice? When might `while` be a better fit?
4. What must eventually happen for a `while` loop to stop?
5. What does `break` do? What does `continue` do?
6. How many times does the inner loop run in this code?

   ```python
   for row in range(3):
       for column in range(4):
           print(row, column)
   ```

7. What is the final value of `total`?

   ```python
   total = 0
   for number in range(1, 5):
       total = total + number
   ```

8. Give one reason to avoid a `while True` loop when a simpler condition can describe the stopping point.
