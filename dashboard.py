import streamlit as st
import streamlit.components.v1 as components

# Dashboardには次のサイトを表示
# レーダーエコー: https://www.jma.go.jp/bosai/nowc/#lat:32.805745/lon:128.463135/zoom:7/colordepth:normal/elements:hrpns&slmcs&slmcs_fcst
# 最新気象情報の降水、風、気温 3日分位を画像貼り付け https://www.data.jma.go.jp/stats/data/mdrr/index.html

st.set_page_config(
        page_title="気象ダッシュボード",
)

"""
### 気象ダッシュボード
"""

"""
#### [レーダーエコー](https://www.jma.go.jp/bosai/nowc/#lat:32.500496/lon:131.176758/zoom:7/colordepth:normal/elements:hrpns&slmcs&slmcs_fcst)
"""

components.iframe(
    src='https://www.jma.go.jp/bosai/nowc/#lat:32.500496/lon:131.176758/zoom:7/colordepth:normal/elements:hrpns&slmcs&slmcs_fcst',
    width=720,
    height=500,
    scrolling=True
)


"""
#### [赤外画像](https://www.jma.go.jp/bosai/map.html#5/34.507/132.166/&elem=ir&contents=himawari)
"""

components.iframe(
    src='https://www.jma.go.jp/bosai/map.html#5/34.507/132.166/&elem=ir&contents=himawari',
    width=720,
    height=500
)

"""
#### [可視画像](https://www.jma.go.jp/bosai/map.html#5/34.507/132.166/&elem=vis&contents=himawari)
"""

components.iframe(
    src='https://www.jma.go.jp/bosai/map.html#5/34.507/132.166/&elem=vis&contents=himawari',
    width=720,
    height=500
)

"""
#### [雲頂強調画像](https://www.jma.go.jp/bosai/map.html#5/31.672/129.902/&elem=strengthen&contents=himawari)
"""

components.iframe(
    src='https://www.jma.go.jp/bosai/map.html#5/31.672/129.902/&elem=strengthen&contents=himawari',
    width=720,
    height=500
)


"""
#### [ウィンドプロファイラ](https://www.jma.go.jp/bosai/map.html#6/30.949/129.276/&contents=windprofiler)
"""

components.iframe(
    src='https://www.jma.go.jp/bosai/map.html#6/30.949/129.276/&contents=windprofiler',
    width=720,
    height=500
)

"""
#### [Windy(950hPa 600m 2000ft)](https://www.windy.com/?950h,32.569,130.627,8)
"""

components.iframe(
    src='https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=default&metricTemp=default&metricWind=default&zoom=7&overlay=wind&product=ecmwf&level=950h&lat=32.695&lon=130.814',
    width=720,
    height=500
)


"""
#### [Windy(900hPa 900m 3000ft)](https://www.windy.com/?900h,32.569,130.627,8)
"""

components.iframe(
    src='https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=default&metricTemp=default&metricWind=default&zoom=7&overlay=wind&product=ecmwf&level=900h&lat=32.695&lon=130.814',
    width=720,
    height=500
)

"""
#### [Windy(850hPa 1500m 5000ft)](https://www.windy.com/?850h,32.569,130.627,8)
"""

components.iframe(
    src='https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=default&metricTemp=default&metricWind=default&zoom=7&overlay=wind&product=ecmwf&level=850h&lat=32.695&lon=130.814',
    width=720,
    height=500
)

"""
#### [SPAS速報天気図](https://www.jma.go.jp/bosai/weather_map/)
"""

components.iframe(
    src='https://www.jma.go.jp/bosai/weather_map/',
    width=720,
    height=850,
    scrolling=True
)

# style（
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)


