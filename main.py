"""Writes one short text, meant to relax the reader, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
import os

TEXT = (
    "The Lamplighter\n"
    "At dusk the lamplighter walks the lane with his long pole, and does not run. "
    "One lamp, a pause, the next. "
    "Behind him the street fills with small warm rooms of light, and the moths arrive unasked. "
    "He is never late. The dark has always waited for him."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit("text length %d is outside 1..280" % len(text))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
