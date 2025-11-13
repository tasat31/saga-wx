import streamlit as st
import streamlit.components.v1 as components


"""
#### [Windy(950hPa 600m 2000ft)](https://www.windy.com/?950h,32.569,130.627,8)
"""

components.iframe(
    src='https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=default&metricTemp=default&metricWind=default&zoom=7&overlay=wind&product=ecmwf&level=950h&lat=32.695&lon=130.814',
    width=720,
    height=500
)


"""
#### [Windy(900hPa 900m 3000ft)](https://www.windy.com/?900h,32.569,130.627,8)
"""

components.iframe(
    src='https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=default&metricTemp=default&metricWind=default&zoom=7&overlay=wind&product=ecmwf&level=900h&lat=32.695&lon=130.814',
    width=720,
    height=500
)

"""
#### [Windy(850hPa 1500m 5000ft)](https://www.windy.com/?850h,32.569,130.627,8)
"""

components.iframe(
    src='https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=default&metricTemp=default&metricWind=default&zoom=7&overlay=wind&product=ecmwf&level=850h&lat=32.695&lon=130.814',
    width=720,
    height=500
)
