from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont

from generate_25_2_figures import CAPTIONS as CAPTIONS_01_10
from generate_25_2_additional_figures import CAPTIONS as CAPTIONS_11_30

HERE = Path(__file__).resolve().parent
SRC = HERE / "figures"
OUT = HERE / "figure_pairs"
OUT.mkdir(parents=True, exist_ok=True)
CAPTIONS = {**CAPTIONS_01_10, **CAPTIONS_11_30}
NAVY = "#102A43"
GREY = "#475569"
TITLE_FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 31)
CAPTION_FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

for first in range(1, 31, 2):
    files = [next(SRC.glob(f"Figure_{n:02d}_*.jpg")) for n in (first, first + 1)]
    images = [Image.open(p).convert("RGB") for p in files]
    height = 1040
    resized = [im.resize((round(im.width * height / im.height), height), Image.Resampling.LANCZOS) for im in images]
    panel_width = max(im.width for im in resized)
    gap = 56
    caption_height = 330
    canvas = Image.new("RGB", (panel_width * 2 + gap, height + caption_height), "white")
    draw = ImageDraw.Draw(canvas)
    for i, im in enumerate(resized):
        number = first + i
        x = i * (panel_width + gap) + (panel_width - im.width) // 2
        canvas.paste(im, (x, 0))
        box_x = i * (panel_width + gap) + 24
        box_y = height + 18
        box_w = panel_width - 48
        draw.rounded_rectangle((box_x, box_y, box_x + box_w, box_y + caption_height - 36), radius=18,
                               fill="#F4F7FA", outline="#CAD5E1", width=2)
        draw.text((box_x + 22, box_y + 18), f"FIGURE {number}", font=TITLE_FONT, fill=NAVY)
        lines = textwrap.wrap(CAPTIONS[number], width=80)
        draw.multiline_text((box_x + 22, box_y + 68), "\n".join(lines), font=CAPTION_FONT,
                            fill=GREY, spacing=7)
    out = OUT / f"Figures_{first:02d}_{first+1:02d}.jpg"
    canvas.save(out, "JPEG", quality=89, optimize=True, progressive=True)
    for im in images:
        im.close()
