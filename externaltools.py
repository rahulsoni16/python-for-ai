
# Pattern 2: Import specific items from a module
from math import sqrt, pi
sqrt(16)


# Ramdom module
import random
number = random.randint(1, 100)
print(number)

choices = ["apple", "banana", "cherry"]
random_choice = random.choice(choices)
print(random_choice)

# Date
from datetime import datetime
current_date = datetime.now()
print(current_date)
print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)
# Format datetime to string (strftime)
# Example output: "April 15, 2026 - 14:30 PM"
formatted_string = current_date.strftime("%B %d, %Y - %H:%M %p")
print(formatted_string)

# timedelta
from datetime import datetime, timedelta

now = datetime.now()

# Add 10 days and 5 hours
future_time = now + timedelta(days=10, hours=5)

# Find the difference between two dates
deadline = datetime(1977, 9, 30)
time_remaining = now - deadline
print("Days remaining:", time_remaining.days)

# 
import os
current_directory = os.getcwd()
print("Current Directory:", current_directory)
