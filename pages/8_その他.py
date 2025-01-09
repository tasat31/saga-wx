import time
import streamlit as st
import datetime

st.set_page_config(
        page_title="その他",
)

"""
### その他

##### 気象庁資料

[気象庁情報カタログ](https://www.data.jma.go.jp/suishin/catalogue/catalogue.html)

[配信資料に関する技術情報](https://www.data.jma.go.jp/add/suishin/cgi-bin/jyouhou/jyouhou.cgi)

##### ご利用にあたっての注意点

- 気象情報の出典は気象庁等からとなります。
- 現在は制作中のサイトのテスト公開となります。
- メンテナンスや修正のため不定期で一時的にアクセスできなくなる場合があります。
- また予告なしにサイト移設・停止する場合があります。

[その他お問い合わせ]

こちらのメールアドレスにお願いします。

info@heart-musen.com

"""

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

