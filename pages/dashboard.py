from datetime import datetime, timezone, timedelta

import streamlit as st
import streamlit.components.v1 as components
from streamlit_carousel import carousel

# Dashboardには次のサイトを表示
# レーダーエコー: https://www.jma.go.jp/bosai/nowc/#lat:32.805745/lon:128.463135/zoom:7/colordepth:normal/elements:hrpns&slmcs&slmcs_fcst
# 最新気象情報の降水、風、気温 3日分位を画像貼り付け https://www.data.jma.go.jp/stats/data/mdrr/index.html

st.set_page_config(
    page_title="気象ダッシュボード",
)

now_utc = datetime.now(timezone.utc)
one_day_ago_utc = now_utc - timedelta(days=1)
next_day_utc = now_utc + timedelta(days=1)

today_month = now_utc.strftime('%Y%m')
one_day_ago_month = one_day_ago_utc.strftime('%Y%m')

today_date = now_utc.strftime('%Y%m%d')
one_day_ago_date = one_day_ago_utc.strftime('%Y%m%d')
next_day_date = next_day_utc.strftime('%Y%m%d')

now_jst = datetime.now()
today_date_jst = now_utc.strftime('%Y%m%d')
today_month_day_jst = now_utc.strftime('%m%d')

# 5時(JST) - 11時(JST)までに閲覧
if now_utc.hour in (19, 20, 22, 23, 0, 1, 2):
    asas_images = [
        dict(
            title=f"ASAS {one_day_ago_date} 0000 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}0000.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}0000.svgz",
        ),
        dict(
            title=f"ASAS {one_day_ago_date} 0600 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}0600.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}0600.svgz",
        ),
        dict(
            title=f"ASAS {one_day_ago_date} 1200 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1200.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1200.svgz",
        ),
        dict(
            title=f"ASAS {one_day_ago_date} 1800 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.svgz",
        ),
    ]

# 12時(JST) - 17時(JST)までに閲覧
elif now_utc.hour in (3, 4, 5, 6, 7, 8):
    asas_images = [
        dict(
            title=f"ASAS {one_day_ago_date} 0600 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}0600.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}0600.svgz",
        ),
        dict(
            title=f"ASAS {one_day_ago_date} 1200 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1200.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1200.svgz",
        ),
        dict(
            title=f"ASAS {one_day_ago_date} 1800 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.svgz",
        ),
        dict(
            title=f"ASAS {today_date} 0000 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0000.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0000.svgz",
        ),
    ]
# 18時(JST) - 23時(JST)までに閲覧
elif now_utc.hour in (9, 10, 11, 12, 13, 14):
    asas_images = [
        dict(
            title=f"ASAS {one_day_ago_date} 1200 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1200.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1200.svgz",
        ),
        dict(
            title=f"ASAS {one_day_ago_date} 1800 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.svgz",
        ),
        dict(
            title=f"ASAS {today_date} 0000 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0000.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0000.svgz",
        ),
        dict(
            title=f"ASAS {today_date} 0600 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0600.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0600.svgz",
        ),
    ]
# 0時(JST) - 3時(JST)までに閲覧 -> 昨日の15時の実況と昨日21時の実況をとる
elif now_utc.hour in (15, 16, 17, 18):
    asas_images = [
        dict(
            title=f"ASAS {one_day_ago_date} 1800 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{one_day_ago_month}/ASAS_COLOR_{one_day_ago_date}1800.svgz",
        ),
        dict(
            title=f"ASAS {today_date} 0000 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0000.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0000.svgz",
        ),
        dict(
            title=f"ASAS {today_date} 0600 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0600.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}0600.svgz",
        ),
        dict(
            title=f"ASAS {today_date} 1200 UTC",
            text="",
            img=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}1200.png",
            link=f"https://www.data.jma.go.jp/yoho/data/wxchart/quick/{today_month}/ASAS_COLOR_{today_date}1200.svgz",
        ),
    ]


latest_wx_images = [
    dict(
        title="降水の状況",
        text="",
        img=f"https://www.data.jma.go.jp/stats/data/mdrr/pre_rct/pic/pre24h{today_month_day_jst}.png",
        link="https://www.data.jma.go.jp/stats/data/mdrr/pre_rct/index24_rct.html",
    ),
    dict(
        title="風の状況",
        text="",
        img=f"https://www.data.jma.go.jp/stats/data/mdrr/wind_rct/pic/mxwsp{today_month_day_jst}.png",
        link="https://www.data.jma.go.jp/stats/data/mdrr/wind_rct/index_mxwsp.html",
    ),
    dict(
        title=f"気温の状況",
        text="",
        img=f"https://www.data.jma.go.jp/stats/data/mdrr/tem_rct/pic/mxtem{today_month_day_jst}.png",
        link="https://www.data.jma.go.jp/stats/data/mdrr/tem_rct/index_mxtem.html",
    ),
    dict(
        title=f"雪の状況",
        text="",
        img=f"https://www.data.jma.go.jp/stats/data/mdrr/snc_rct/pic/snc{today_month_day_jst}.png",
        link="https://www.data.jma.go.jp/stats/data/mdrr/snc_rct/index_snc.html",
    ),
]

st.write(f"{now_utc.strftime('%Y / %m /%d %H:%M')} UTC 現在")

if st.button("Refresh", key="refresh_top"):
    st.rerun()

"""
### 気象概況

"""

st.write("[[ASAS] アジア太平洋域 実況天気図](https://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/ASAS_COLOR.pdf)")

st.pdf('https://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/ASAS_COLOR.pdf')

with st.expander("実況天気の推移"):
    st.caption("[過去の実況天気図](https://www.data.jma.go.jp/yoho/wxchart/quickmonthly.html)、[SPAS速報天気図](https://www.jma.go.jp/bosai/weather_map/)")

    carousel(items=asas_images)

    st.caption("ASASは日本時間 3時、9時、15時、21時に発出")

with st.expander("最新の気象データ"):
    carousel(items=latest_wx_images)

st.write("[[FSAS24] アジア地上 24時間天気図](https://www.data.jma.go.jp/yoho/data/wxchart/quick/FSAS24_COLOR_ASIA.pdf)")

st.pdf('https://www.data.jma.go.jp/yoho/data/wxchart/quick/FSAS24_COLOR_ASIA.pdf')

"""
##### [レーダーエコー](https://www.jma.go.jp/bosai/nowc/#lat:32.500496/lon:131.176758/zoom:7/colordepth:normal/elements:hrpns&slmcs&slmcs_fcst)
"""



himawari_col1, himawari_col2 = st.columns(2)

with himawari_col1:
    """
    ##### [赤外画像](https://www.jma.go.jp/bosai/map.html#5/34.507/132.166/&elem=ir&contents=himawari)
    """
    hour_and_minute = (now_utc - timedelta(minutes=20)).strftime('%H%M')[0:3] + '0'
    st.image(f"https://www.data.jma.go.jp/mscweb/data/himawari/img/jpn/jpn_b13_{hour_and_minute}.jpg")

with himawari_col2:
    """
    ##### [可視画像](https://www.jma.go.jp/bosai/map.html#5/34.507/132.166/&elem=vis&contents=himawari)
    """

    st.image(f"https://www.data.jma.go.jp/mscweb/data/himawari/img/jpn/jpn_tre_{hour_and_minute}.jpg")

"""
##### [雲頂強調画像](https://www.jma.go.jp/bosai/map.html#5/31.672/129.902/&elem=strengthen&contents=himawari)
"""

"""
##### [エマグラム](https://weather.uwyo.edu/upperair/seasia.html)
"""

if now_utc.hour in (0, 1, 2, 3):
    previous_emagram_fukuoka_image_url = f"https://weather.uwyo.edu/upperair/images/{one_day_ago_date}00.47807.stuve700.parc.gif"
    previous_emagram_kagoshima_image_url = f"https://weather.uwyo.edu/upperair/images/{one_day_ago_date}00.47827.stuve700.parc.gif"

    latest_emagram_fukuoka_image_url = f"https://weather.uwyo.edu/upperair/images/{one_day_ago_date}12.47807.stuve700.parc.gif"
    latest_emagram_kagoshima_image_url = f"https://weather.uwyo.edu/upperair/images/{one_day_ago_date}12.47827.stuve700.parc.gif"
elif now_utc.hour in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):
    previous_emagram_fukuoka_image_url = f"https://weather.uwyo.edu/upperair/images/{one_day_ago_date}12.47807.stuve700.parc.gif"
    previous_emagram_kagoshima_image_url = f"https://weather.uwyo.edu/upperair/images/{one_day_ago_date}12.47827.stuve700.parc.gif"

    latest_emagram_fukuoka_image_url = f"https://weather.uwyo.edu/upperair/images/{today_date}00.47807.stuve700.parc.gif"
    latest_emagram_kagoshima_image_url = f"https://weather.uwyo.edu/upperair/images/{today_date}00.47827.stuve700.parc.gif"
elif now_utc.hour in (15, 16, 17, 18, 19, 20, 21, 22, 23):
    previous_emagram_fukuoka_image_url = f"https://weather.uwyo.edu/upperair/images/{today_date}00.47807.stuve700.parc.gif"
    previous_emagram_kagoshima_image_url = f"https://weather.uwyo.edu/upperair/images/{today_date}00.47827.stuve700.parc.gif"

    latest_emagram_fukuoka_image_url = f"https://weather.uwyo.edu/upperair/images/{today_date}12.47807.stuve700.parc.gif"
    latest_emagram_kagoshima_image_url = f"https://weather.uwyo.edu/upperair/images/{today_date}12.47827.stuve700.parc.gif"

with st.expander("鹿児島、福岡", expanded=True):
    st.write("鹿児島")

    col_ema_kagoshima_1, col_ema_kagoshima_2 = st.columns(2)
    with col_ema_kagoshima_1:
        st.caption("前回")
        st.image(previous_emagram_kagoshima_image_url)

    with col_ema_kagoshima_2:
        st.caption("最新")
        st.image(latest_emagram_kagoshima_image_url)

    st.write("福岡")

    col_ema_fukuoka_1, col_ema_fukuoka_2 = st.columns(2)
    with col_ema_fukuoka_1:
        st.caption("前回")
        st.image(previous_emagram_fukuoka_image_url)

    with col_ema_fukuoka_2:
        st.caption("最新")
        st.image(latest_emagram_fukuoka_image_url)

if st.button("Refresh", key="refresh_bottom"):
    st.rerun()

# style（
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)


