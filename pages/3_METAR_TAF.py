import streamlit as st
import streamlit.components.v1 as components
from settings import MY_STATIONS
from services.aviationweather import get_wx

station_ids = MY_STATIONS.split(',')
wx = get_wx(station_ids)

st.set_page_config(
        page_title="METAR, TAF, 飛行場時系列データ",
)

"""
### METAR, TAF, 飛行場時系列データ

METAR, TAFの読み方: [航空気象通報式第3版](https://www.jma.go.jp/jma/kishou/books/tsuhoshiki/koukuu/koukuu3_15.pdf)

"""
if st.button("Refresh", key="refresh_top"):
    st.rerun()

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

    with st.expander("飛行場時系列予報・飛行場時系列情報・航空気象解説情報"):
        st.image(f"https://www.data.jma.go.jp/airinfo/data/pict/taf/QMCD98_{station_id}.png")
        st.image(f"https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_{station_id}.png")

if st.button("Refresh", key="refresh_bottom"):
    st.rerun()

"""
出典:
    気象庁・飛行場気象解説情報（定時/臨時）: https://www.data.jma.go.jp/airinfo/data/awfo_comment.html
"""
# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
