"""Writes one short text, meant to relax the reader, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
import os

TEXT = (
    "The Ferryman\n"
    "The river is wide and the ferryman is in no hurry. "
    "The rope runs through his hands, one hand, then the other. "
    "Mist lifts off the water in pieces. "
    "The far bank comes closer the way a name does once you stop reaching for it. "
    "The boat has always known the way."
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
