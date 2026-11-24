"""Funniest Time Machine Warning Label - make.fun one-liner entry.

Writes the warning-label line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only - the grader runs bare
python:3.13, so no third-party imports are used here.
"""

import os

LINE = (
    "WARNING: Do not meet your younger self, or the timeline will be "
    "hotfixed and you will be the bug that gets rolled back."
)


def main() -> None:
    # One-liner budget: a single beat, 90-153 bytes total.
    encoded = LINE.encode("utf-8")
    if not 90 <= len(encoded) <= 153:
        raise ValueError(f"entry is {len(encoded)} bytes, outside 90-153")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
    else:
        path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
