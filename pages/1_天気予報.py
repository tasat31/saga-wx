import streamlit as st
import streamlit.components.v1 as components
from app.widgets.jma_weekly_latest import JmaWeeklyLatest

jma_weekly_latest = JmaWeeklyLatest(st)

st.set_page_config(
        page_title="日本全国 天気予報",
)

"""
### 日本全国 天気予報
"""
jma_weekly_latest.render()

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
