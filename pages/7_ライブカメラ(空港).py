import time
import streamlit as st
import datetime

st.set_page_config(
        page_title="その他",
)

"""
### ライブカメラ(空港)
"""

# 福江空港

st.video('https://youtu.be/5sHKk-kBnJc')

# 長崎空港

st.video('https://youtu.be/Q6xrfvPbYkk')

# 福岡空港

st.video('https://youtu.be/Cw91vSGfmRc')

# 熊本空港

st.video('https://youtu.be/rGtE0C62fss')

# 鹿児島空港

st.video('https://youtu.be/sGHH_ujdIto')

# 奄美空港

st.video('https://youtu.be/mBT1zJZQp7s')

# 大分空港

st.video('https://youtu.be/Gtm0yLkFdXs')

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

