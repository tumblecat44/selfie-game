"""
SONGSONG - Selfie to Face Cipher Converter
Usage: python selfie2seq.py <image_path> [size]
  size: grid size (default 8 = 8x8 = 64 numbers)
"""
import sys
from PIL import Image

def selfie_to_sequence(path, size=8):
    img = Image.open(path).convert("RGB").resize((size, size))
    pixels = list(img.getdata())
    # Each pixel -> single value (weighted grayscale-ish, but keeping full 0-255 range)
    seq = [int(r * 0.4 + g * 0.35 + b * 0.25) for r, g, b in pixels]
    return seq

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python selfie2seq.py <image_path> [grid_size]")
        sys.exit(1)

    path = sys.argv[1]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seq = selfie_to_sequence(path, size)

    print(f"[{', '.join(map(str, seq))}]")
    print(f"\n# {len(seq)} values from {size}x{size} grid")
