import time
import streamlit as st

"""
### 毎時大気解析

出典:
    毎時大気解析: https://www.data.jma.go.jp/airinfo/data/awfo_maiji.html

"""

img_arrays = [
    "https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_20240227090000.PNG",
    "https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_20240227100000.PNG",
    "https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_20240227110000.PNG",
    "https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_20240227120000.PNG",
    "https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_20240227130000.PNG",
    "https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_20240227140000.PNG",
    "https://www.data.jma.go.jp/airinfo/data/pict/maiji/WANLC156_RJTD_20240227150000.PNG",
]

placeholder = st.empty()

for img_array in img_arrays:
  placeholder.image(img_array, width=1000)
  time.sleep(3)


# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

