<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>Article_Scraping</h1>
    <p>各プログラムの説明を下記に記す。</p>
    <h3>各プログラムの説明</h3>
    <dl>
      <dt>1.URL_scraping.py:</dt>
      <dd>Yahoo経済新聞ホームページから最新記事15本のURLを取得し、csvファイルにindex-日付-title-URLの形式で書き込みます。<br>
          ファイル名は自動的に「本プログラムが実行された日時.csv」で保存されます。</dd>
      <dt>2.Article_scraping.py:</dt>
      <dd>URL_Scraping.pyで取得したURLにアクセスして、そのURLに記述された記事内容を取得する。<br>
          その後、csvファイルにindex/title/記事内容の形式で書き込まれます。<br>
          ※管理しやすようにファイル名には、プログラムを実行した日付が必ず入力されます。</dd>
   </dl>
   <h3>実行コマンドと実行順序</h3>
   <p>※同じフォルダ内に両方のプログラムがある状態</p>
   <ol>
      <li>python3 URL_scraping.py </li>
      <li>python3 Article_scraping.py </li>
   </ol>
   <h3>使用したライブラリ一覧</h3>
   <ul>
      <li>bs4</li> 
      <li>pandas</li>
   </ul>
 </body>
</html>
