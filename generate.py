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

FONT_FILE = (
    "NotoSansJP-VariableFont_wght.ttf"
)

WIDTH = 300
HEIGHT = 60


# ==========================
# 初期化
# ==========================

os.makedirs(
    OUT_DIR,
    exist_ok=True
)


font = ImageFont.truetype(
    FONT_FILE,
    22
)


# ==========================
# JSON取得
# ==========================

print("JSON取得")

r = requests.get(
    JSON_URL,
    timeout=10
)

r.raise_for_status()

data = r.json()


if not data:
    print("データなし")
    exit()


# 最新3件
items = data[-3:]

# 新しい順
items = items[::-1]


# ==========================
# 画像生成
# ==========================

for index, item in enumerate(items):

    title = item.get(
        "title",
        "No Title"
    )


    # ----------------------
    # 16文字制限
    # ----------------------

    if len(title) > 16:

        title = (
            title[:16]
            + "..."
        )


    # ----------------------
    # 画像作成
    # ----------------------

    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "white"
    )


    draw = ImageDraw.Draw(img)


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


# 4枚目以降削除
for i in range(4,20):

    old = (
        f"{OUT_DIR}/title{i}.png"
    )

    if os.path.exists(old):

        os.remove(old)
