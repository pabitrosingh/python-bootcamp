# Week 4 quiz answers - Recursion and integration

1. The base case returns without another recursive call; the recursive step calls the function with a smaller or simpler problem.
2. Without progress, the function may never reach a stopping condition and will keep consuming call-stack space.
3. `RecursionError`.
4. No. Python does not perform tail-call optimization.
5. `0`, the explicitly chosen empty-input base case.
6. Iteration usually avoids call-stack limits and is often simpler for linear repetition.
7. Any four of: object/dictionary, array/list, string, number, boolean, and `null`/`None`.
8. Importing should make definitions available without unexpected file I/O or side effects; file access belongs in an explicit function or the program's main workflow.
