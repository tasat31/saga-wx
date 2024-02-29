import time
import streamlit as st
import datetime

"""
### 毎時大気解析

出典:
    毎時大気解析: https://www.data.jma.go.jp/airinfo/data/awfo_maiji.html

"""

st.session_state.airinfo_pictures = []

current_datetime_utc = datetime.datetime.now(datetime.timezone.utc)

for hours in range(9, 0, -1):
    past_datetime = current_datetime_utc - datetime.timedelta(hours=hours)
    picture_url = 'https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_%s0000.PNG' % past_datetime.strftime("%Y%m%d%H")
    st.session_state.airinfo_pictures.append(picture_url)

placeholder = st.empty()

for pict in st.session_state.airinfo_pictures:
  placeholder.image(pict, width=1000)
  time.sleep(3)

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

