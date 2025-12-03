import streamlit as st

st.set_page_config(
    page_title="週間天気予報",
)

"""
### 週間天気予報
##### 出典: [気象庁|数値予報天気図](https://www.jma.go.jp/bosai/numericmap/)
"""

tab1, tab2, tab3 = st.tabs([
    "FEFE19 週間アンサンブル予想図",
    "FZCX50 週間予報支援図（アンサンブル）",
    "FXXN519 週間予報支援図"
])

with tab1:
    st.image('https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fefe19.png')

with tab2:
    st.image('https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fzcx50.png')

with tab3:
    st.image('https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fxxn519.png')
