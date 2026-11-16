# Exercise 2 - Process a batch of CPU work

Write a module-level function that counts prime numbers below a supplied limit. Use `ProcessPoolExecutor.map()` to process several limits.

Requirements:

- Put the launch code in a `main()` function.
- Guard the entry point with `if __name__ == "__main__":`.
- Compare process-pool results with sequential results.
- Ensure that each task's inputs and result can be transferred between processes.
- Explain why the process pool might not help for tiny limits.
