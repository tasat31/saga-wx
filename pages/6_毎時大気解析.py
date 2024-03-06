import time
import streamlit as st
import datetime

"""
### 毎時大気解析

出典:
    毎時大気解析: https://www.data.jma.go.jp/airinfo/data/awfo_maiji.html

"""

st.session_state.airinfo_time_series_pictures = []
st.session_state.airinfo_flight_level_pictures = []

current_datetime_utc = datetime.datetime.now(datetime.timezone.utc)

for hours in range(9, 0, -1):
    past_datetime = current_datetime_utc - datetime.timedelta(hours=hours)
    picture_url = 'https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_%s0000.PNG' % past_datetime.strftime("%Y%m%d%H")
    st.session_state.airinfo_time_series_pictures.append(picture_url)

latest_datetime = past_datetime

for flight_level in ['21', '19', '17', '15', '13', '11', '09', '07', '05']:
    st.session_state.airinfo_flight_level_pictures.append(
        'https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLF1%s_RJTD_%s0000.PNG' % (flight_level, latest_datetime.strftime("%Y%m%d%H"))
    )

time_series_placeholder = st.empty()
flight_level_placeholder = st.empty()

for i in range(9):
  time_series_placeholder.image(st.session_state.airinfo_time_series_pictures[i], width=1000)
  flight_level_placeholder.image(st.session_state.airinfo_flight_level_pictures[i], width=1000)
  time.sleep(3)

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

