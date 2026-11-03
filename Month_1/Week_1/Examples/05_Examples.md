# Month 1 / Week 1: Putting the basics together

This example asks for a name, a number of study sessions, and minutes per session. It converts the numeric text, calculates total study time, and formats the result.

```python
name = input("What is your name? ").strip()
sessions_text = input("How many sessions did you complete? ")
minutes_text = input("How many minutes was each session? ")

sessions = int(sessions_text)
minutes_per_session = int(minutes_text)
total_minutes = sessions * minutes_per_session

print(f"{name}, you studied for {total_minutes} minutes this week.")
```

Try changing the calculation to display hours as well. Use `total_minutes / 60` and format the result to one decimal place with `:.1f`.

This version assumes valid input. Handling invalid numeric input is covered in Week 4.