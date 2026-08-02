def check_weather(temperature, city):
    # temperature = 30
    if temperature > 25:
        message = f"It's Hot! in {city}"
        return message
    else:
        message = f"Nice weather in {city}"
        return message


print(check_weather(temperature=16, city="Bangalore"))  


# returning multiple values from a function
def simple_function():
   numbers = [1, 2, 3, 4, 5]
   first_number = numbers[0]
   last_number = numbers[-1]
   return first_number, last_number

first, last = simple_function()
print(f"First number: {first}, Last number: {last}")