# Week 1 / Example 1 - Define a class and create instances

A class groups data and operations that belong together. Each call to the class creates a separate instance:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says woof"


first = Dog("Milo")
second = Dog("Luna")
print(first.speak())
print(second.name)
```

`__init__` initializes a new instance. `self.name` is stored on that instance, so `first.name` and `second.name` can differ. The method call `first.speak()` is equivalent to `Dog.speak(first)`.

**Try it:** Add a `breed` value and a method that returns a short description. Create two instances and confirm their values are independent.
