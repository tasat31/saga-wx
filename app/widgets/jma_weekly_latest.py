import os, base64, uuid
import urllib.request
import urllib.error
from PyPDF2 import PdfWriter

_urls = [
    {
        'url': 'https://www.data.jma.go.jp/fcd/yoho/data/jishin/kaisetsu_tanki_latest.pdf',
        'description':
            """
            #### [短期予報解析資料](https://www.data.jma.go.jp/fcd/yoho/data/jishin/kaisetsu_tanki_latest.pdf)
            """
    },
    {
        'url': 'https://www.data.jma.go.jp/fcd/yoho/data/jishin/kaisetsu_shukan_latest.pdf',
        'description':
            """
            #### [週間天気予報解説資料](https://www.data.jma.go.jp/fcd/yoho/data/jishin/kaisetsu_shukan_latest.pdf)
            """
    },
]

class JmaWeeklyLatest:

    def __init__(self, st):
        self.st = st

    def render(self):
        download_tmp_files = []

        for url in _urls:
            try:
                file = urllib.request.urlretrieve(url['url'])[0]
                self.st.markdown(url['description'])
                with open(file, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

                pdf_display = pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="900" height="700" type="application/pdf">'

                self.st.markdown(pdf_display, unsafe_allow_html=True)

                download_tmp_files.append(file)
            except urllib.error.HTTPError:
                pass

        for file in download_tmp_files:
            try:
                os.remove(file)
            except Exception as e:
                pass
