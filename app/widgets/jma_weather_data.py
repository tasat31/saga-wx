import os, base64, uuid
import urllib.request
import urllib.error
from PyPDF2 import PdfWriter

_urls = [
    {
        'url': 'https://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/ASAS_MONO.pdf',
        'description':
            """
            ##### [ASAS] アジア太平洋域 実況天気図
            観測時刻時点の実況で気圧配置や前線等の概観を確認します。
            詳細の説明は[こちら](https://www.jma.go.jp/jma/kishou/know/kurashi/ASAS_kaisetu.html)
            """
    },
    {
        'url': 'https://www.data.jma.go.jp/fcd/yoho/data/wxchart/quick/FSAS24_MONO_ASIA.pdf',
        'description':
            """
            ##### [FSAS24] アジア地上 24時間天気図
            実況天気図をもとに、気圧配置や前線等の動きについて予想を行います。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/aupq35_00.pdf',
        'description':
            """
            ##### [AUPQ35] アジア500hPa・300hPa高度・気温・風・等風速線天気図
            500hPa,300hPa高層の実況図で、トラフや寒冷渦等の確認を行います。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/aupq78_00.pdf',
        'description':
            """
            ##### [AUPQ78] アジア850hPa・700hPa高度・気温・風・湿数天気図
            850hPa,700hPa高層の実況図で、湿域等の確認を行います。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/axfe578_00.pdf',
        'description':
            """
            ##### [AXFE578] 極東850hPa気温・風、700hPa上昇流／500hPa高度・渦度天気図
            850hPa,700hPa高層の数値解析図で、渦度、上昇流等の確認を行います。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fupa502_00.pdf',
        'description':
            """
            ##### [FUPA502] アジア太平洋500hPa 高度・気温・風 24時間予想図
            500hPa高層の数値予報図で、トラフや寒冷渦等の発現を確認し、擾乱の予想等を行います。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fxfe502_00.pdf',
        'description':
            """
            ##### [FXFE502] 極東地上気圧・風・降水量／500hPa高度・渦度予想図
            500hPa高層の数値予報図で、渦度、降水量の予想等を行います。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fxfe5782_00.pdf',
        'description':
            """
            ##### [FXFE5782] 極東850hPa気温・風、700hPa上昇流／700hPa湿数、500hPa気温予想図 24時間予想図
            700hPaの上昇流の予想を行います。上昇流の発生と湿数から降水や雲の発生を予想します。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/fxjp854_00.pdf',
        'description':
            """
            ##### [FXJP854] 日本850hPa相当温位・風予想図
            前線や高気圧の縁辺を沿って吹き込む風の向きや温位を予想します。
            """
    },
    {
        'url': 'https://www.jma.go.jp/bosai/numericmap/data/nwpmap/feas502_12.pdf',
        'description':
            """
            ##### [FEAS502] アジア地上気圧、850hPa気温／500hPa高度・渦度 24時間予想図
            500hPaの渦度の数値予報にもとづいて、前線やシアラインの発現を予想します。
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
                self.st.markdown(url['description'])
                with open(file, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

                pdf_display = pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="900" height="700" type="application/pdf">'

                self.st.markdown(pdf_display, unsafe_allow_html=True)

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
