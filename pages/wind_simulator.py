import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="風向風速シミュレータ",
)

wind_directions = ('北:N', '北北東:NNE', '北東:NE', '東北東:ENE', '東:E', '東南東:ESE', '南東:SE', '南南東:SSE', '南:S', '南南西:SSW', '南西:SW', '西南西:WSW', '西:W', '西北西:WNW', '北西:NW', '北北西:NNW')

dict_wind_directions_degrees = {
    '北:N': '360', '北北東:NNE': '020', '北東:NE': '050', '東北東:ENE': '070',
    '東:E': '090', '東南東:ESE': '110', '南東:SE': '140', '南南東:SSE': '160',
    '南:S': '180', '南南西:SSW': '200', '南西:SW': '230', '西南西:WSW': '250',
    '西:W': '270', '西北西:WNW': '290', '北西:NW': '320', '北北西:NNW': '340'
}

"""
### 風向風速シミュレータ(エクマン層)
"""

"""
##### 1. ウィンドプロファイラ観測値入力
"""
(col_hirado, col_kumamoto, col_ichiki) = st.columns(3)

with col_hirado:
    hirado_wind_velocity = st.number_input(
        "平戸(高度1km)", value=None, placeholder="風速(m/s)"
    )
    hirado_wind_direction = st.selectbox(
        "平戸(高度1km)", wind_directions, index=None
    )

with col_kumamoto:
    kumamoto_wind_velocity = st.number_input(
        "熊本(高度1km)", value=None, placeholder="風速(m/s)"
    )
    kumamoto_wind_direction = st.selectbox(
        "熊本(高度1km)", wind_directions, index=None
    )

with col_ichiki:
    ichiki_wind_velocity = st.number_input(
        "市来(高度1km)", value=None, placeholder="風速(m/s)"
    )
    ichiki_wind_direction = st.selectbox(
        "市来(高度1km)", wind_directions, index=None
    )

"""
##### 2. Observation Map観測値入力
"""
(col_unzen, col_yatsushiro, col_makinohara) = st.columns(3)
with col_unzen:
    unzen_wind_velocity = st.number_input(
        "雲仙(高度678m)", value=None, placeholder="風速(m/s)"
    )
    unzen_wind_direction = st.selectbox(
        "雲仙(高度678m)", wind_directions, index=None
    )

with col_yatsushiro:
    yatsuhiro_wind_velocity = st.number_input(
        "八代(高度8m)", value=None, placeholder="風速(m/s)"
    )
    yatsuhiro_wind_direction = st.selectbox(
        "八代(高度8m)", wind_directions, index=None
    )

with col_makinohara:
    unzen_wind_velocity = st.number_input(
        "牧之原(高度387m)", value=None, placeholder="風速(m/s)"
    )
    unzen_wind_direction = st.selectbox(
        "牧之原(高度387m)", wind_directions, index=None
    )

"""
##### 3. 自由大気層の風の予想(850hPaの風予想等)
"""
(col_ariake_bay, col_yatsushiro_bay, col_kinko_bay) = st.columns(3)
with col_ariake_bay:
    ariake_bay_wind_velocity = st.number_input(
        "有明海(5000ft)", value=None, placeholder="風速(m/s)"
    )
    ariake_bay_wind_direction = st.selectbox(
        "有明海(5000ft)", wind_directions, index=None
    )

with col_yatsushiro_bay:
    yatsushiro_bay_wind_velocity = st.number_input(
        "八代海(5000ft)", value=None, placeholder="風速(m/s)"
    )
    yatsushiro_bay_wind_direction = st.selectbox(
        "八代海(5000ft)", wind_directions, index=None
    )

with col_kinko_bay:
    kinko_bay_wind_velocity = st.number_input(
        "錦江湾(5000ft)", value=None, placeholder="風速(m/s)"
    )
    kinko_bay_wind_direction = st.selectbox(
        "錦江湾(5000ft)", wind_directions, index=None
    )


df_waypoint = pd.DataFrame(
    {
        "竹崎": [85, 3, 2, 1, 1,1],
        "大牟田": [2, 78, 4, 0, 1,1],
        "八代": [1, 5, 72, 3, 1,1],
        "薩摩川内": [0, 2, 1, 89, 1,1],
    },
    index=["surface", "2,000ft", "2,500f", "3,500ft", "4,500ft", "5,500ft"],
)
st.table(df_waypoint)
