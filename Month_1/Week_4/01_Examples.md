# Week 4 / Example 1 - Define and call a function

Define a function with `def`, then call it by writing its name followed by parentheses.

```python
def show_welcome():
    print("Welcome to the Python bootcamp!")


show_welcome()
show_welcome()
```

The function body is indented. Defining it does not run it; each call runs the body once.

Give a function a parameter when its behavior depends on a value:

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Asha")
greet("Noah")
```