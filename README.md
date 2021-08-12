# Article_Scraping
各プログラムの説明を下記に記す。
<br>
1. URL_scraping.py:<br>
Yahoo経済新聞ホームページ(https://news.yahoo.co.jp/topics/business)から最新記事15本のURLを取得し、csvファイルにindex-日付-title-URLの形式で書き込みます。
ファイル名は自動的に「実行された日時.csv」で保存されます。
<br>

2. Article_scraping.py:<br>
URL_Scraping.pyで取得したURLにアクセスして、そのURLに記述された記事内容を取得する。
その後、csvファイルにindex/title/記事内容の形式で書き込まれます。
<br>
※管理しやすようにファイル名には、プログラムを実行した日付が必ず入力されます。

<br>
＜実行用ライブラリ＞<br>
・bs4 
・pandas

