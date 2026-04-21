import streamlit as st
import pandas as pd

from src.predict import satellite_downscaling
from src.api_weather import get_weather

if st.button("Satellite AQI (Downscaled)"):

    weather = get_weather(city)

    if weather is None:
        st.error("Weather not available")
    else:
        temp, humidity = weather

        data = satellite_downscaling(temp, humidity)

        st.subheader("🛰️ Satellite-Based AQI Grid")

        df = pd.DataFrame(data)

        st.dataframe(df)

        st.write("Showing AQI predictions across city grid (downscaled)")
from src.predict import generate_report

st.set_page_config(layout="wide")

st.title("🌍 Advanced AQI Intelligence System")

city = st.text_input("Enter City", "Delhi")

if st.button("Generate Full AQI Report"):

    data = generate_report(city)

    if data is None:
        st.error("Data not available")
    else:
        for d in data:
            st.subheader(f"📍 {d['location']}")

            st.write(f"AQI: {d['aqi']}")
            st.write(f"Pollution Score: {d['score']}")
            st.write(f"Area Type: {d['area']}")

            st.write("7-Day Forecast:")
            st.write(d["forecast"])

            st.write(f"Reason: {d['reason']}")

            st.markdown("---")