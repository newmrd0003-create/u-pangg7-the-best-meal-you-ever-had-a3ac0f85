#!/usr/bin/env python3
"""The Best Meal You Ever Had (u-pangg7-the-best-meal-you-ever-had-a3ac0f85).

Writes exactly one sentence about the best meal ever had to
/output/entry.txt. Deterministic: the same sentence every run.
"""

import os

SENTENCE = (
    "At Warung Bu Tini in Yogyakarta, the soto ayam came steaming, "
    "lemongrass and fried shallots in every spoonful, and I ate it "
    "standing in the rain because every plastic chair was taken."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
