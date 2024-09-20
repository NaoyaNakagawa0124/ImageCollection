import requests
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

# ブログのURL
url = 'https://sakurazaka46.com/s/s46/diary/detail/57068?ima=0000&cd=blog'

# ウェブページの取得
response = requests.get(url)
response.encoding = response.apparent_encoding  # エンコーディングの設定
html = response.text

# BeautifulSoupでHTML解析
soup = BeautifulSoup(html, 'html.parser')

# ブログ本文の抽出（クラス名やタグは実際のHTML構造に合わせて調整が必要です）
content = soup.find('div', class_='box-article').get_text(strip=True)

print("抽出されたテキスト：")
print(content)

# 感情分析の簡易実装
positive_words = ['嬉しい', '楽しい', '幸せ', 'ありがとう', '大好き']
negative_words = ['悲しい', '辛い', '嫌い', 'ごめん', '寂しい']

tokenizer = Tokenizer()
tokens = tokenizer.tokenize(content)

positive_score = 0
negative_score = 0

for token in tokens:
    word = token.surface
    if word in positive_words:
        positive_score += 1
    elif word in negative_words:
        negative_score += 1

print("\n感情分析結果：")
print(f"ポジティブな単語の数: {positive_score}")
print(f"ネガティブな単語の数: {negative_score}")
