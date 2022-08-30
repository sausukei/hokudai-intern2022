import lxml.html
from lxml.html.clean import Cleaner

# ダウンロードしたXHTMLファイルのファイル名を書きます。
# ちなみに1567_14913.htmlは《走れメロス》です。
FILE_NAME = '江戸川乱歩 怪人二十面相.html'

f = open(FILE_NAME, encoding='shift_jis')
data = f.read().encode('shift_jis')
f.close()

cleaner = Cleaner(page_structure=False, remove_tags=('ruby', 'br'), kill_tags=('rt', 'rp'))
cln_html = cleaner.clean_html(data).decode('utf-8')

plain_text = lxml.html.fromstring(cln_html).find_class('main_text')[0].text_content()
print(plain_text)

with open("clean.txt", mode='w') as f:
    f.write(plain_text)