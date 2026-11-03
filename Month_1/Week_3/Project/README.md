# Mini project - Password Strength Checker

Build a command-line checker that reports which basic password rules a candidate meets. This is a learning exercise, not a production security validator.

## Rules

Check whether the password:

- Has at least 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit

## Requirements

- Ask for one candidate password.
- Use a loop to inspect its characters and track which rules are met.
- Display each rule as passed or not yet met.
- Give a final result of `Strong` only if all four rules pass; otherwise show `Needs improvement`.
- Do not print or store the entered password.

## Acceptance checklist

- [ ] Check empty, short, long, mixed-case, and digit-free examples.
- [ ] A password with all four properties passes.
- [ ] Each failed rule is explained.
- [ ] The output never repeats the password.

Do not claim that these rules guarantee a password is secure. Real password security also depends on length, uniqueness, storage, and the service's authentication design.
