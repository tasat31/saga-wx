import os, base64, uuid
import urllib.request
import urllib.error
from PyPDF2 import PdfWriter

_urls = [
    {
        'title': '[ASAS] アジア太平洋域 実況天気図',
        'url': 'https://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/ASAS_MONO.pdf',
        'description':
            """
           詳細の説明は[こちら](https://www.jma.go.jp/jma/kishou/know/kurashi/ASAS_kaisetu.html)
            """
    },
    {
        'title': '[FSAS24] アジア地上 24時間天気図',
        'url': 'https://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/FSAS24_MONO_ASIA.pdf',
        'description':
            """
            """
    },
    {
        'title': '[AUPQ35] アジア500hPa・300hPa高度・気温・風・等風速線天気図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/aupq35_00.pdf',
        'description':
            """
            """
    },
    {
        'title': '[AUPQ78] アジア850hPa・700hPa高度・気温・風・湿数天気図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/aupq78_00.pdf',
        'description':
            """
            """
    },
    {
        'title': '[AXFE578] 極東850hPa気温・風、700hPa上昇流／500hPa高度・渦度天気図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/axfe578_00.pdf',
        'description':
            """
            """
    },
    {
        'title': '[FXFE502] 極東地上気圧・風・降水量／500hPa高度・渦度予想図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fxfe502_00.pdf',
        'description':
            """
            """
    },
    {
        'title': '[FXFE5782] 極東850hPa気温・風、700hPa上昇流／700hPa湿数、500hPa気温予想図 24時間予想図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fxfe5782_00.pdf',
        'description':
            """
            """
    },
    {
        'title': '[FXJP854] 日本850hPa相当温位・風予想図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fxjp854_00.pdf',
        'description':
            """
            """
    },
    {
        'title': ':white_check_mark: [FUPA502] アジア太平洋500hPa 高度・気温・風 24時間予想図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fupa502_00.pdf',
        'description':
            """
            """
    },
    {
        'title': ':white_check_mark: [FEAS502] アジア地上気圧、850hPa気温／500hPa高度・渦度 24時間予想図',
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/feas502_12.pdf',
        'description':
            """
            """
    },

]

class JmaWeatherData:

    def __init__(self, st):
        self.st = st

    def render(self):

        merger = PdfWriter()
        download_tmp_files = []

        for url in _urls:
            try:
                file = urllib.request.urlretrieve(url['url'])[0]
                self.st.subheader(url['title'], divider='rainbow')
                with open(file, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

                pdf_display = pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="900" height="700" type="application/pdf">'

                self.st.markdown(pdf_display, unsafe_allow_html=True)

                self.st.markdown(url['description'])

                merger.append(file)
                download_tmp_files.append(file)
            except urllib.error.HTTPError:
                pass

        output_file_path = "/tmp/%s.pdf" % uuid.uuid4().hex[:8]
        output = open(output_file_path, "wb")
        merger.write(output)
        merger.close()
        output.close()

        with open(output_file_path, "rb") as file:
            self.st.download_button(
                label="気象データをまとめてダウンロード",
                data=file,
                file_name="jma_chart.pdf",
                mime="application/pdf"
            )

        for file in download_tmp_files:
            try:
                os.remove(file)
            except Exception as e:
                pass

        """
        出典:
            高層天気図: https://www.jma.go.jp/bosai/numericmap/#type=upper
            数値予報天気図: https://www.jma.go.jp/bosai/numericmap/
        """
