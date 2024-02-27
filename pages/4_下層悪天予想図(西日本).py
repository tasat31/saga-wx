import streamlit as st
import streamlit.components.v1 as components

"""
### 下層悪天予想図(西日本)

"""

st.image("https://www.data.jma.go.jp/airinfo/data/pict/low-level_sigwx/fbos39.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/low-level_sigwx/fbos03.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/low-level_sigwx/fbos06.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/low-level_sigwx/fbos09.png")


"""
出典:
    気象庁・下層悪天予想図: https://www.data.jma.go.jp/airinfo/data/awfo_low-level_sigwx.html
"""

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
