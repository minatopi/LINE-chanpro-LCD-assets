import os
import requests
from PIL import Image, ImageDraw, ImageFont


# ==========================
# 設定
# ==========================

JSON_URL = (
    "https://minatopi.github.io/"
    "LINE-chanpro-Surveillance/output.json"
)

OUT_DIR = "images"

FONT_FILE = "NotoSansJP-VariableFont_wght.ttf"

WIDTH = 300
HEIGHT = 60


# ==========================
# 初期化
# ==========================

os.makedirs(
    OUT_DIR,
    exist_ok=True
)


# フォント
font = ImageFont.truetype(
    FONT_FILE,
    22
)


# ==========================
# JSON取得
# ==========================

print("JSON取得")

r = requests.get(JSON_URL)

r.raise_for_status()

data = r.json()


if len(data) == 0:
    exit()


# 最新3件
items = data[-3:]


# 古い→新しい
items = items[::-1]


# ==========================
# 画像生成
# ==========================

for index, item in enumerate(items):

    title = item.get(
        "title",
        "No Title"
    )


    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "white"
    )


    draw = ImageDraw.Draw(img)


    # 長すぎる文字を切る
    while (
        draw.textlength(
            title,
            font=font
        ) > WIDTH - 10
    ):
        title = title[:-1]


    draw.text(
        (5,18),
        title,
        fill=(0,0,0),
        font=font
    )


    filename = (
        f"{OUT_DIR}/title{index+1}.png"
    )


    img.save(filename)

    print(
        "作成:",
        filename
    )
