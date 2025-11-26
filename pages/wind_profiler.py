import streamlit as st

import folium
from streamlit_folium import st_folium, folium_static

"""
#### [ウィンドプロファイラ](https://www.jma.go.jp/bosai/map.html#6/30.949/129.276/&contents=windprofiler)と[Observation Map](https://www.jma.go.jp/bosai/map.html#8/33.305/130.109/&elem=wind&contents=amedas&lang=en&interval=10)
"""


wind_profiler_url="https://www.jma.go.jp/bosai/windprofiler/"
wind_profiler_stations = [
  {"location": [33.36, 129.55], "code": 47805, "name": "平戸"},
  {"location": [32.81, 130.71], "code": 47819, "name": "熊本"},
  {"location": [31.71, 130.32], "code": 47848, "name": "市来"},
  {"location": [32.58, 131.66], "code": 47822, "name": "延岡"},
  {"location": [33.24, 131.62], "code": 47815, "name": "大分"},
]

observation_url = "https://www.jma.go.jp/bosai/amedas/"

observation_areas = [
 {"location": [33.3417, 129.7117], "area_code": 420000, "amdno": 84183, "name": "松浦"},
 {"location": [33.1483, 130.3017], "area_code": 410000, "amdno": 85176, "name": "川副"},
 {"location": [32.917, 129.913], "area_code": 420000, "amdno": 84371, "name": "大村"},
 {"location": [32.737, 130.2617], "area_code": 420000, "amdno": 84519, "name": "雲仙岳"},
 {"location": [32.8317, 131.013], "area_code": 430000, "amdno": 86157, "name": "南阿蘇"},
 {"location": [32.4733, 130.607], "area_code": 430000, "amdno": 86336, "name": "八代"},
 {"location": [31.803, 130.718], "area_code": 460100, "amdno": 88166, "name": "溝辺"},
 {"location": [31.6617, 130.843], "area_code": 460100, "amdno": 88286, "name": "牧之原"},
]

attr = (
    '<a href="https://maps.gsi.go.jp/development/ichiran.html" target="_blank">地理院タイル</a>'
)

tiles = "https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg"


wind_profiler_kw = {"prefix": "fa", "color": "green", "icon": "arrow-up"}
observation_kw = {"prefix": "fa", "color": "purple", "icon": "arrow-up"}

m = folium.Map(location=[32.519026,130.734558], tiles=tiles, attr=attr, zoom_start=8)


fg_wind_profiler_station = folium.FeatureGroup(name="wind profiler station")

for station in wind_profiler_stations:

    angle = 90 # Todo: wind_directionを設定する
    icon = folium.Icon(angle=angle, **wind_profiler_kw)

    fg_wind_profiler_station.add_child(folium.Marker(
        location=station["location"],
        popup=f'<a href="{wind_profiler_url}#code={station["code"]}&type=chart" target="_blank">{station["name"]}</a>',
        icon=icon,
        tooltip=f"{station["name"]}")
    )

m.add_child(fg_wind_profiler_station)

fg_observation_area = folium.FeatureGroup(name="observation area")

for observation_area in observation_areas:

    angle = 90 # Todo: wind_directionを設定する
    icon = folium.Icon(angle=angle, **observation_kw)

    fg_observation_area.add_child(folium.Marker(
        location=observation_area["location"],
        popup=f'<a href="{observation_url}#area_type=offices&area_code={observation_area["area_code"]}&amdno={observation_area["amdno"]}&format=graph&lang=en&elem=wind" target="_blank">{observation_area["name"]}</a>',
        icon=icon,
        tooltip=f"{observation_area["name"]}")
    )

m.add_child(fg_observation_area)

st_folium(m, width=800, key="wind_map", returned_objects=[])
