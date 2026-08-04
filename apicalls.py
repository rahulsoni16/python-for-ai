import requests


def get_weather(latitude, longitude):

    # Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    # Make the request
    response = requests.get(url)
    data = response.json()

    temp = data.get("current").get("temperature_2m")
    temp_unit = data.get("current_units").get("temperature_2m")

    return temp, temp_unit


paris_temp = get_weather(48.5,2.35)
london_temp = get_weather(51.50,-0.12)
home_temp = get_weather(12.84,77.65)

    
print(f"Current Temperature in Paris: {paris_temp}")
print(f"Current Temperature in London: {london_temp}")
print(f"Current Temperature in London: {home_temp}")





