from datetime import datetime, timedelta

# Current date and time
now = datetime.now()

# Extracting components
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
weekday = now.weekday()  # 0: Monday, 6: Sunday
iso = now.isocalendar()  # ISO year, week number, and weekday.

# Formatted strings using f-string
formatted_date = f"{now:%Y-%m-%d}"
formatted_time = f"{now:%H:%M:%S}"
formatted_full = f"{now:%A}, {now:%B} {now.day}, {now.year}"

# Calculate next week's date
next_week = now + timedelta(weeks=1)
print(iso)

# Output results
print(f"Formatted Date: {formatted_date}")
print(f"Formatted Time: {formatted_time}")
print(f"Formatted Full: {formatted_full}")
print(f"Next week's date: {next_week}")
print(f"Day of the week: {now.strftime('%A')}")
print(f"Is it weekend? {'Yes' if weekday >= 5 else 'No'}")
