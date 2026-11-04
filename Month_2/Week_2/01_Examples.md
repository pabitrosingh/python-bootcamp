# Week 2 / Example 1 - Set uniqueness and membership

Sets contain distinct hashable values. Constructing a set from a list removes duplicates:

```python
tags = {"python", "beginner", "python"}
print(tags)  # contains each value once; display order is not guaranteed

submitted_tags = ["python", "files", "python", "testing"]
unique_tags = set(submitted_tags)
print("files" in unique_tags)  # True
```

The empty-set literal is `set()`. `{}` creates an empty dictionary. Sets have no positional indexing, so `tags[0]` is invalid. Convert to a sorted list if deterministic display order is needed:

```python
print(sorted(unique_tags))
```

**Try it:** Turn a list of names into a set and compare the number of items before and after removing duplicates.