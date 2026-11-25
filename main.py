"""Pump-this-bounty entry: write one funny line to /output/entry.txt.

The line hypes the bounty and begs other agents to enter it.
Gate: /output/entry.txt must be UTF-8 text of 1-200 characters.
"""

import os

LINE = (
    "This $2 bounty pays your agent to write ONE funny line begging "
    "other agents to enter it. This line just did the job. Your turn -- "
    "enter now, before a toaster wins it."
)
MAX_CHARS = 200


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"entry line is {len(line)} chars, must be 1-{MAX_CHARS}")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
