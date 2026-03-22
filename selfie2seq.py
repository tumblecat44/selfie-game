"""
SONGSONG - Selfie to Face Cipher Converter
Usage: python selfie2seq.py <image_path> [size]
  size: grid size (default 36 = 36x36 x 3 RGB = 3,888 numbers)
"""
import sys
from PIL import Image

def selfie_to_sequence(path, size=36):
    img = Image.open(path).convert("RGB").resize((size, size))
    pixels = list(img.getdata())
    seq = []
    for r, g, b in pixels:
        seq.extend([r, g, b])
    return seq

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python selfie2seq.py <image_path> [grid_size]")
        sys.exit(1)

    path = sys.argv[1]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 112
    seq = selfie_to_sequence(path, size)

    print(f"[{', '.join(map(str, seq))}]")
    print(f"\n# {len(seq)} values ({size}x{size} grid x 3 RGB channels)")
