import requests

response = requests.get('https://api.github.com')
print(response.status_code)

name = "Alice"
print(f"Hello, {name.lower()}!")

age = 24

3*4


long_string = """This is a long string that spans multiple lines.
It can be used to store large amounts of text without needing to use escape characters for newlines
or other special characters. This is useful for documentation, multi-line messages, or any situation where
you need to include literal newlines in your string."""
first_name = "John"
last_name = "Doe"

full_name = f"{first_name} {last_name}"

long_dash = "-"*30

print(long_dash)
len(long_dash)

is_logged_in = True
# String manipulation

message = "I love programming in Python!"

print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())

new_message = message.replace("Python", "JavaScript")
print(new_message)

# Conditional statements
temperature = 17
if temperature > 20:
    print("It's a warm day.")
elif temperature > 10:
    print("It's a cool day.")
else:
    print("It's a cold day.")


score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")    


# Loops
for i in range(5):
    print(f"Iteration {i+1}")

for i in range(1, 6):
    print(f"Square of {i} is {i**2}")    

for i in range(1,10,2):
    print(f"Odd number: {i}")


# error handling
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 
finally:
    print("Execution completed.")
