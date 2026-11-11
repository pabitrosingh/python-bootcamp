# Week 2 / Example 2 - Substitution and small interfaces

A subtype must honor the promises made by its base type. If callers expect every `Bird` to fly, a penguin subtype violates that contract. Model only the shared behavior that is actually valid:

```python
class Animal:
    def eat(self):
        return "eating"


class FlyingAnimal(Animal):
    def fly(self):
        return "flying"


class Sparrow(FlyingAnimal):
    pass


class Penguin(Animal):
    pass
```

This design also avoids forcing all animals to implement operations they cannot perform (Interface Segregation). For ordinary Python code, small protocols or simple collaborators can express roles without a deep inheritance tree.

**Try it:** Model a document reader and a document printer as separate capabilities. Which client needs each one?
