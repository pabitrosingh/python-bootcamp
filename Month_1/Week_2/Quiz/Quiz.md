# Week 2 quiz - Decisions

Try every question before checking [Answers.md](./Answers.md).

1. What is the value of `2 + 3 * 4`? How could you make the addition happen first?
2. What type of value does `age >= 18` produce?
3. What is the difference between `=` and `==`?
4. When is `and` true? When is `or` true?
5. What does `not False` evaluate to?
6. Why should a grade program test `score >= 90` before `score >= 80`?
7. What message does this program print for `balance = 20` and `amount = 30`?

   ```python
   if amount <= 0:
       print("Invalid")
   elif amount > balance:
       print("Insufficient")
   else:
       print("Approved")
   ```

8. Write a condition that is true when `temperature` is between 10 and 25 inclusive.
9. In an `if`/`elif`/`else` ladder, what happens when two conditions are true?
10. When is a nested `if` useful? When would an `elif` ladder be clearer?
11. Rewrite this assignment with a conditional expression:

    ```python
    if score >= 60:
        result = "pass"
    else:
        result = "retry"
    ```

12. What happens if no case in a `match` statement matches and there is no `case _`?
13. In a `match` statement, what is the purpose of `case _`?
14. Is an empty string (`""`) true or false in an `if` condition? Is the non-empty string `"False"` true or false?
15. Why does this guard avoid dividing by zero?

    ```python
    denominator != 0 and 10 / denominator > 1
    ```
