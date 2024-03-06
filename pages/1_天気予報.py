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

"""
#### [短期予報解説資料](https://www.data.jma.go.jp/fcd/yoho/data/jishin/kaisetsu_tanki_latest.pdf)
"""


"""
#### [NHKニュース | 気象動画](https://www.data.jma.go.jp/fcd/yoho/data/jishin/kaisetsu_tanki_latest.pdf)
"""

components.iframe(
    src='https://www3.nhk.or.jp/news/weather/weather_movie.html',
    width=720,
    height=500
)

components.iframe(
    src='https://www.jma.go.jp/bosai/map.html#5/29.478/131.309/&contents=forecast',
    width=720,
    height=500
)

jma_weekly_latest.render()

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
