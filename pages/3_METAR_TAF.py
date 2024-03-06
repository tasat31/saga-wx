import streamlit as st
import streamlit.components.v1 as components
from settings import MY_STATIONS
from services.aviationweather import get_wx

station_ids = MY_STATIONS.split(',')
wx = get_wx(station_ids)

"""
### METAR, TAF, 飛行場時系列データ

METAR, TAFの読み方: [航空気象通報式第3版](https://www.jma.go.jp/jma/kishou/books/tsuhoshiki/koukuu/koukuu3_15.pdf)

"""
for station_id in station_ids:
    st.subheader(station_id, divider='rainbow')
    if (wx[station_id]['metar']['text'] == ''):
        st.code("No Metar reported")
    else:
        st.code(wx[station_id]['metar']['text'])

    if (wx[station_id]['metar']['text'] == ''):
        st.code("No TAF reported")
    else:
        st.code(wx[station_id]['taf']['text'])

    st.image("https://www.data.jma.go.jp/airinfo/data/pict/taf/QMCD98_%s.png" % (station_id))

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
