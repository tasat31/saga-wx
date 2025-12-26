import time
import streamlit as st
import datetime

st.set_page_config(
        page_title="早見表・換算ツール",
)


"""
### 早見表・換算ツール
"""

tab1, tab2, tab3 = st.tabs([
    "hPa -> inchHg",
    "Pressure Altitude(ft) and Density Altitude(ft)",
    "m <-> ft",
])

with tab1:
    """
    [pressureConversion](https://www.weather.gov/media/epz/wxcalc/pressureConversion.pdf)
    """

    val_hPa = st.number_input("hPa", format="%.2f", value=1013.25, key="hPa")
    val_inchHg = val_hPa / 33.8689

    st.write(f"{val_inchHg:.2f} inches")

with tab2:
    val_pressure = st.number_input("QNH inchHg(at MSL)", format="%.2f", value=29.92, key="QNH")
    elevation = st.number_input("elevation(ft)", format="%d", value=6)

    pressure_altitude = (29.92 - val_pressure) * 1000 + elevation

    st.write(f"Pressure Altitude = {pressure_altitude:.1f} ft")

    oat = st.number_input("OAT Outside Air Temperture(Celsius)", format="%d", value=15, key="OAT")

    densitiy_altidude = pressure_altitude + 120 * (oat - (15 - (elevation / 1000) * 2))

    st.write(f"Density Altitude = {densitiy_altidude:.1f} ft")

with tab3:
    val_ft = st.number_input("distance(ft)", format="%d", value=500, key="feet")
    st.write(f"distance(m) = {val_ft * 0.3048} m")

    val_meter = st.number_input("distance(m)", format="%d", value=150, key="meter")
    st.write(f"distance(m) = {val_meter * 3.2808390} m")
