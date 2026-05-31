# Month 1 / Week 1: Day 1 — Variables & Basic Data Types

Today we are covering how Python stores information and the four most fundamental data types you will use every single day.

## 1. What is a Variable?
A variable is a named container used to store data values. In Python, you create a variable simply by giving it a name and assigning a value using the `=` operator.

```python
# Assigning values to variables
username = "Pabitro"
bootcamp_duration_months = 6

print(username)
print(bootcamp_duration_months)
We will focus on two foundational concepts: Variables (how Python remembers things) and Data Types (the kinds of things it can remember).

📖 The Concept
Think of a variable like a labeled storage box. You can put something inside the box, give the box a name, and change its contents whenever you want. The data type defines exactly what kind of item you are putting inside that box

## 2. The Core 4 Data Types
Python automatically figures out what kind of data you are giving it. Here are the primary types:

A. Strings (str)
Used for text. Strings must always be wrapped in single (') or double (") quotes.

greeting = "Hello, Python world!"

B. Integers (int)
Whole numbers, positive or negative, without decimals.

current_year = 2026
temperature = -5

C. Floats (float)
Numbers with a decimal point. Crucial for precise measurements or financial data.

pi_value = 3.14159
price = 19.99

D. Booleans (bool)
Logical values that can only be either True or False. (Note the capital T and F!).

is_coding_fun = True
is_finished = False

## 3. Checking Data Types: The type() Function
If you are ever unsure what data type a variable is holding, Python provides a built-in helper called type().

score = 100
print(type(score))  # Output: <class 'int'>

name = "Alice"
print(type(name))   # Output: <class 'str'>

