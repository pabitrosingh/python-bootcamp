# Month 1 / Week 1: Day 3 — User Input & Type Casting

Today we are learning how to make our Python programs interactive by capturing user inputs, and how to convert data between different types (Type Casting).

---

## 1. Capturing User Input
Python uses the built-in `input()` function to pause code execution and wait for the user to type something into the terminal.

> ⚠️ **CRITICAL RULE:** The `input()` function **always** reads user input as a String (`str`), even if the user types a number!

### Asking for a text input
```python
favorite_food = input("What is your favorite food? ")
print(f"Oh awesome, I love {favorite_food} too!")
```
### Capturing a number (Notice what happens next)
```python
age = input("Enter your age: ")
print(type(age))  # Output: <class 'str'>
```

## 2. Type Casting (Data Conversion)
Because input() treats everything as text, we cannot do math with it immediately. If a user inputs "25", we have to convert that text string into a real integer. This conversion process is called Type Casting.

We use functions named exactly after the data types: int(), float(), str(), and bool().

### A. Converting String to Integer / Float

#### Converting user input string to integer to do math
```python
birth_year_input = input("What year were you born? ")  # Example: "2000"
birth_year = int(birth_year_input)                    # Casts "2000" (str) to 2000 (int)
current_year = 2026
calculated_age = current_year - birth_year
print(f"You are roughly {calculated_age} years old!")
```
### B. Converting Numbers to Strings
Sometimes you need to treat numbers as strings.
```python
lucky_number = 7

#Converting integer to string so we can combine it with text safely
announcement = "My lucky number is " + str(lucky_number)
print(announcement)
```
## 3. Putting It Together: A Simple Calculator Example
Here is how you can use input and casting together to build a functional command-line script:

```python
# Get inputs from the user
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

# Convert inputs to floats so they handle decimals smoothly
total = float(num1_str) + float(num2_str)

print(f"The exact sum of those numbers is: {total}")
```
