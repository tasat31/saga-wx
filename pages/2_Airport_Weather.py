import streamlit as st
import streamlit.components.v1 as components
from settings import MY_STATIONS
from services.aviationweather import get_wx

station_ids = MY_STATIONS.split(',')
wx = get_wx(station_ids)

"""
### 空港 気象

"""
for station_id in station_ids:
    st.markdown(wx[station_id]['metar']['text'])
    st.markdown(wx[station_id]['taf']['text'])
    st.image("https://www.data.jma.go.jp/airinfo/data/pict/taf/QMCD98_%s.png" % (station_id))

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
