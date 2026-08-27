from pathlib import Path
from PIL import Image, ImageOps


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "scientific_story_infographics"
OUT = HERE / "scientific_story_pairs"


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(SOURCE.glob("Story_*.jpg"))
    if len(files) != 20:
        raise RuntimeError(f"Expected 20 story infographics, found {len(files)}")
    outputs = []
    for pair_index in range(10):
        left_path, right_path = files[pair_index * 2: pair_index * 2 + 2]
        with Image.open(left_path) as left_source, Image.open(right_path) as right_source:
            left = left_source.convert("RGB")
            right = right_source.convert("RGB")
            height = max(left.height, right.height)
            if left.height != height:
                left = ImageOps.pad(left, (left.width, height), color="white")
            if right.height != height:
                right = ImageOps.pad(right, (right.width, height), color="white")
            gap = 24
            plate = Image.new("RGB", (left.width + right.width + gap, height), "white")
            plate.paste(left, (0, 0))
            plate.paste(right, (left.width + gap, 0))
            first = pair_index * 2 + 1
            output = OUT / f"Stories_{first:02d}_{first+1:02d}.jpg"
            plate.save(output, "JPEG", quality=87, optimize=True, progressive=True)
            outputs.append(output)
    return outputs


if __name__ == "__main__":
    for path in build():
        print(path)
