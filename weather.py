import requests
import streamlit as st
import plotly.express as px

# OpenWeatherMap API Key
api_key = "4dec903e0dd58ee0c89b6dfdb0a45470"  # Make sure to use quotes

# Title of the app
st.title("Weather Forecasting App")

# Input for City with unique key
city = st.text_input("Enter city name (e.g., Chicago,US):", key="city_input")

# Function to fetch weather data
def get_weather_data(city, api_key):
    # Corrected line below
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Fetch and display data when the city name is entered
if city:
    data = get_weather_data(city, api_key)

    # Inspect the full API response for debugging
    st.write(data)

    if data.get("cod") == 200:  # Check if the city is found (cod 200 means OK)
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        st.write(f"### Weather in {city}")
        st.write(f"**Temperature**: {temp}°C")
        st.write(f"**Humidity**: {humidity}%")
        st.write(f"**Wind Speed**: {wind_speed} m/s")

        # Visualization example
        weather_info = {
            "Temperature": temp,
            "Humidity": humidity,
            "Wind Speed": wind_speed,
        }
        fig = px.bar(x=weather_info.keys(), y=weather_info.values(), title=f"Weather Data for {city}")
        st.plotly_chart(fig)
    else:
        error_message = data.get("message", "City not found")
        st.error(f"City '{city}' not found. Please try again. Error: {error_message}")
        
                                   