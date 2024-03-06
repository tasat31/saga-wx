import streamlit as st

st.set_page_config(
        page_title="航空気象解説情報",
)

"""
### 航空気象解説情報

"""

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFS.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFU.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFT.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFK.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFO.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFM.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFF.png")

st.image("https://www.data.jma.go.jp/airinfo/data/pict/comment/ADJH01_RJFR.png")

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

