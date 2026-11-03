# Month 1 project - Calculator

Build a command-line calculator for two numbers and one arithmetic operation.

## Requirements

- Ask for two numbers and an operation: addition, subtraction, multiplication, or division.
- Accept `+`, `-`, `*`, and `/` as operation symbols.
- Display the result clearly.
- Explain that division by zero is not allowed.
- Explain when the user enters an unsupported operation.

This project practices variables, input, numeric conversion, arithmetic, conditionals, and formatted output. It assumes that number inputs are valid; add `ValueError` handling after studying Week 4.

## Example

```text
First number: 12
Operation (+, -, *, /): /
Second number: 4
Result: 3.00
```

## Run and test

From this directory, run:

```bash
python calculator.py
python -m unittest -v
```

## Acceptance checklist

- [ ] Each of the four operations returns the expected result.
- [ ] Division by zero shows a helpful message instead of crashing.
- [ ] An unsupported operation shows a helpful message.
- [ ] Test positive, negative, decimal, and zero values.
