import streamlit as st
from app.widgets.jma_weather_data import JmaWeatherData

jma_weather_data = JmaWeatherData(st)

st.set_page_config(
        page_title="気象庁 天気図",
)

"""
### 気象庁 天気図

気象庁からWeather Briefing用の資料を取得
"""

jma_weather_data.render()

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
