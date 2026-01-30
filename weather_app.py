import streamlit as st
import requests

# =============================
# OPENWEATHER API CONFIG
# =============================
API_KEY = "7cfa67cbc15468a5ac9ae8b14ad6bc9c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# =============================
# STREAMLIT PAGE SETUP
# =============================
st.set_page_config(page_title="Weather Prediction App", page_icon="🌦️")

st.title("🌦️ Weather Prediction App")
st.write("Enter a city name to get real-time weather details")

# =============================
# USER INPUT
# =============================
city = st.text_input("City Name")

# =============================
# BUTTON LOGIC
# =============================
if st.button("Get Weather"):
    if city.strip() == "":
        st.warning("Please enter a city name")
    else:
        params = {
            "q": city,
            "appid": API_KEY
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            temperature_c = round(data["main"]["temp"] - 273.15, 2)

            st.success(f"Weather in {city}")
            st.write(f"🌡️ Temperature: {temperature_c} °C")
            st.write(f"💧 Humidity: {data['main']['humidity']} %")
            st.write(f"🔽 Pressure: {data['main']['pressure']} hPa")
            st.write(f"☁️ Condition: {data['weather'][0]['description']}")

        else:
            st.error("❌ API key not authorized or city not found")
            st.write("Status code:", response.status_code)
