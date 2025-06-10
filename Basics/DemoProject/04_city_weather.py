# This is  a demo project to show know your city weather using Python.

import requests

# Description: A simple weather management system that allows checking the weather of a city.
# This uses the WeatherAPI to fetch current weather data for a specified city.
# It prompts the user to enter a city name and displays the current weather conditions.

# http://api.weatherapi.com/v1/forecast.json?key=68e4cc7430524cf6a26110422250906&q=noida&days=3&aqi=no&alerts=no
base_url = "http://api.weatherapi.com/v1/forecast.json?"  # Base URL for the WeatherAPI
api_key = "68e4cc7430524cf6a26110422250906"  # Replace with your OpenWeatherMap API key  

my_city = input("Enter your city name: ") 

final_weather_url =  f"{base_url}key={api_key}&q={my_city}&days=3&aqi=no&alerts=no"


response = requests.get(final_weather_url)

if response.status_code == 200:
    data = response.json()
    city_name = data.get('location').get('name')
    country = data.get('location').get('country')
    temperature = data.get('current').get('temp_c')
    condition = data.get('current').get('condition').get('text')
    
    # Print the current weather information
    # It retrieves the city name, country, current temperature, and weather condition from the JSON response
    print(f"\nToday's Weather in {city_name}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Weather Condition: {condition}")

   
    print(f"\nForecast for the next 3 days weather in {city_name}, {country}:")
    # Loop through the forecast data for the next 3 days
    # It retrieves the date, maximum temperature, minimum temperature, and weather condition for each day
    for day in data.get('forecast').get('forecastday'):
        date = day.get('date')
        max_temp = day.get('day').get('maxtemp_c')
        min_temp = day.get('day').get('mintemp_c')
        condition = day.get('day').get('condition').get('text')
        # Print the date, maximum temperature, minimum temperature, and weather condition for each day
        print(f"{date}: Max Temp: {max_temp}°C, Min Temp: {min_temp}°C, Condition: {condition}")

else:
    print("City not found or API request failed. Please check the city name and try again.")

