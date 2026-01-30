import streamlit as st
import requests

st.set_page_config(page_title="World Weather App", page_icon="🌍")
st.title("🌍 World Weather App")

API_KEY = "7cfa67cbc15468a5ac9ae8b14ad6bc9c"  # Replace with your OpenWeather API key

city = st.text_input("Enter city (e.g., London, UK)")

if st.button("Check Weather"):
    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data["cod"] == 200:
            st.success(f"Weather in {city}")
            st.write("🌡️ Temperature:", data["main"]["temp"], "°C")
            st.write("☁️ Condition:", data["weather"][0]["description"])
            st.write("💧 Humidity:", data["main"]["humidity"], "%")
            st.write("🌬️ Wind Speed:", data["wind"]["speed"], "m/s")
            st.write("Data provided by OpenWeatherMap.org")
        else:
            st.error("City not found. Try city,country")
    else:
        st.warning("Please enter a city name")
