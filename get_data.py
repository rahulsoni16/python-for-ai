import requests
from datetime import datetime, timedelta
import pandas as pd

import matplotlib.pyplot as plt

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
# 12.84,77.65
# Get Bangalore weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=12.84&longitude=77.65&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

#---------- Pandas DataFrame ----------
daily_data = data["daily"]

df = pd.DataFrame({
    'date' : daily_data['time'],
    'min_temp' : daily_data['temperature_2m_min'],
    'max_temp' : daily_data['temperature_2m_max']
})
df['date'] = pd.to_datetime(df['date'])

print(df)

#-------matplotlib-----


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

#------csv file-----
import os

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/bangalore_weather.csv', index=False)
print("Data saved to data/bangalore_weather.csv")