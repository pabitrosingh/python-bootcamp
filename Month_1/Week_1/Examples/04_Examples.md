# Week 1 / Day 5 - Format entered values

`input()` always returns text, even when the person types digits. Convert that text before using it as a number.

```python
name = input("What is your name? ")
age_text = input("How old are you? ")

age = int(age_text)
next_year_age = age + 1
print(f"Hello, {name.strip()}! Next year you will be {next_year_age}.")
```

Convert to `float` when decimal values are useful, such as a measurement or price:

```python
price_text = input("Enter the price: ")
price = float(price_text)
print(f"Price: ${price:.2f}")
```

The conversion raises `ValueError` if the text is not a valid number. Week 4 will show how to handle that error. For now, enter a valid whole number or decimal.

## Check your understanding

1. What type does `input()` return?
2. Why does `int(input("Age: "))` fail if the person enters `ten`?

Answers: `input()` returns `str`; `int()` cannot convert the word `ten` to an integer.
