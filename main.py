import streamlit as st

st.set_page_config(
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.sidebar.title("My Local Weather Insight")
st.sidebar.caption("Heart Musen LLC 2025")

pg = st.navigation({
    "Home": [
        st.Page("pages/dashboard.py", title="dashboard", icon=":material/home:"),
        # st.Page("pages/settings.py", title="設定", icon=":material/settings:"),
    ],
    "気象庁発表":[
        st.Page("pages/2_気象庁天気図.py", title="気象庁天気図", icon=":material/add_circle:"),
        st.Page("pages/1_天気予報.py", title="天気予報", icon=":material/add_circle:"),
        st.Page("pages/3_METAR_TAF.py", title="METER/TAF", icon=":material/add_circle:"),
        st.Page("pages/4_下層悪天予想図(西日本).py", title="下層悪天予想図(西日本)", icon=":material/add_circle:"),
        st.Page("pages/6_毎時大気解析.py", title="毎時大気解析", icon=":material/add_circle:"),
    ],
    "風の予測": [
        st.Page("pages/wind_profiler.py", title="ウィンドプロファイラ", icon=":material/add_circle:"),
        st.Page("pages/windy.py", title="Windy", icon=":material/add_circle:"),
    ],
    "ライブカメラ":[
        st.Page("pages/7_ライブカメラ(空港).py", title="ライブカメラ(空港)", icon=":material/add_circle:"),
    ],
    "その他":[
        st.Page("pages/8_その他.py", title="免責事項", icon=":material/extension:"),
    ],
})
pg.run()
