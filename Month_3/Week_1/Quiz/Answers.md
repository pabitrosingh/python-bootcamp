# Week 1 quiz answers - Object-oriented programming

1. A class defines a type's behavior and structure; an instance is one object created from that class.
2. The instance the method was called on.
3. Instance attributes belong to one object. Class attributes are defined on the class and are shared unless shadowed on an instance.
4. The list is shared by instances. Create it inside `__init__` so each object gets its own list.
5. It signals an implementation detail by convention. Python does not prevent callers from accessing it.
6. When the subtype genuinely satisfies the behavior promised by the base type (an “is a” relationship).
7. Composition means an object holds or uses another object. A fake collaborator can replace the real one in a test.
8. Examples include `__init__`, `__repr__`, and `__eq__`. Annotations do not enforce runtime types or values by themselves.
