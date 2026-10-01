"""答案を送る のアイコン（青地に紙と右向きの矢印）を 180/192/512px で作る。"""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent
for n in (180, 192, 512):
    s = 512
    im = Image.new("RGB", (s, s), "#2b6cb0")
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((110, 80, 330, 400), 18, fill="white")          # 答案の紙
    for y in (150, 200, 250, 300):
        d.line((150, y, 290, y), fill="#9fb8d6", width=14)
    d.polygon([(300, 300), (400, 300), (400, 255), (470, 340), (400, 425), (400, 380), (300, 380)], fill="#ffd34d")  # PCへ
    im.resize((n, n), Image.LANCZOS).save(OUT / f"icon-{n}.png")
print("ok")
