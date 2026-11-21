"""Writes one short text, meant to relax the reader, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
import os

TEXT = (
    "The kettle does not hurry the water. It hums, and waits, "
    "and the steam rises when it is ready. Nothing here is late. "
    "Read this the way light crosses a floor, slowly, asking nothing of the dust. "
    "Whatever comes next, you can walk to it at the speed of morning."
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
