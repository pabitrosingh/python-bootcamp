# Month 1 / Week 1: Day 2 — Basic Math Operations & String Manipulation

Today we are learning how to perform mathematical calculations using numbers, and how to combine or modify text strings.

---

## 1. Basic Math Operations (Arithmetic)
Python works beautifully as a calculator. Here are the main operators you will use:

```python
x = 10
y = 3

# Addition (+)
print(x + y)  # Output: 13

# Subtraction (-)
print(x - y)  # Output: 7

# Multiplication (*)
print(x * y)  # Output: 30

# Division (/) -> Always returns a float!
print(x / y)  # Output: 3.3333333333333335

# Floor Division (//) -> Divides and rounds down to the nearest whole number
print(x // y) # Output: 3

# Modulo (%) -> Returns the remaining remainder of a division
print(x % y)  # Output: 1 (Because 3 goes into 10 three times, with 1 left over)

# Exponentiation (**) -> Power/Indices
print(x ** y) # Output: 1000 (10 to the power of 3)
```

## 2. String Manipulation (Working with Text)
You can modify and combine strings in Python using some very simple tricks.

### A. String Concatenation (Joining Strings)
You can use the + sign to glue strings together.

```python
first_name = "Pabitro"
last_name = "Singh"
```

#### Combining strings (adding a space in the middle)

```python
full_name = first_name + " " + last_name
print(full_name)  # Output: Pabitro Singh
```
### B. String Replication (Multiplying Text)
You can use the * sign to repeat a string multiple times.

```python
cheer = "Go! "
print(cheer * 3)  # Output: Go! Go! Go!
```

### C. F-Strings (Formated Strings) - The Best Way to Output Text
Instead of using + to join text and variables, you can put an f right before your string quotes and use curly brackets {} to inject variables directly.

```python
age = 25
# This is much cleaner than: "I am " + str(age) + " years old."
message = f"Hello, my name is {first_name} and I am {age} years old."
print(message)
```
