# Week 1 / Example 2 - Instance and class attributes

Instance attributes describe one object. A class attribute is shared by instances that do not override it:

```python
class Employee:
    organization = "Acme"

    def __init__(self, name):
        self.name = name


ada = Employee("Ada")
grace = Employee("Grace")
print(ada.organization, grace.organization)

ada.organization = "New Acme"
print(ada.organization)       # instance attribute shadows the class attribute
print(grace.organization)     # still reads the class attribute
print(Employee.organization)  # class attribute is unchanged
```

Avoid mutable class attributes for per-instance data:

```python
class BadTeam:
    members = []  # shared by every BadTeam instance
```

Put each instance's list in `__init__` instead: `self.members = []`.

**Try it:** Create two teams and add a member to only one. Confirm their member lists do not affect each other.
