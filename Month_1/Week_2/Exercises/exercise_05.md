# Exercise 5 - Command selector with `match`

Requires Python 3.10 or newer. Ask the user for a command: `help`, `start`, `pause`, or `quit`. Use `match`/`case` to print a different response for each command and `case _` for an unknown command. Ignore letter case by normalizing the input with `.lower()`.

**Test:** Try all four valid commands, a command with uppercase letters, and `restart`.

**Try next:** Make `start` and `resume` select the same branch with an OR pattern (`case "start" | "resume":`).

For Python versions older than 3.10, implement the same behavior with `if`/`elif`/`else`.
