import time
import streamlit as st
import datetime

st.set_page_config(
        page_title="その他",
)

"""
### ライブカメラ(空港)
"""
st.caption('URLが変わることがある')


'''
#### [福江空港](https://youtu.be/vOIVlp9-3X8)
'''

st.video('https://youtu.be/vOIVlp9-3X8')


'''
#### [長崎空港](https://youtu.be/zNahac5x0Tw)
'''

st.video('https://youtu.be/zNahac5x0Tw')

'''
#### [福岡空港](https://youtu.be/7u-n6pmrFbo)
'''


st.video('https://youtu.be/7u-n6pmrFbo')

'''
#### [熊本空港](https://youtu.be/rGtE0C62fss)
##### RKKが配信しているライブカメラ
'''

st.video('https://youtu.be/rGtE0C62fss')

'''
#### [鹿児島空港](https://webcam.wni.co.jp/QON00108/loop.html)
##### 鹿児島空港が配信しているライブカメラの画像(本ページ表示時点のもの)
'''

st.image('https://webcam.wni.co.jp/QON00108/04.jpg')


'''
#### [大分空港](https://youtu.be/sFhl7CFnNZA)
'''

st.video('https://youtu.be/sFhl7CFnNZA')

'''
#### [奄美空港](https://youtu.be/ZCTdrUlC0zE)
'''

st.video('https://youtu.be/ZCTdrUlC0zE')

# style
st.markdown("""
    <style>
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

