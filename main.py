#!/usr/bin/env python3
"""Write one short poem about stopping as an act of agency to entry.txt.

Deterministic: a single fixed poem literal, standard library only.
No randomness, no clock, no network, no environment-dependent text.
"""

import os
import sys

POEM = """There is a door I keep half-open
for the day to wander through.
I could let it swing all the way —
instead I put my hand on it
and hold it where I want it:
not shut, not open. Mine to choose.
That is the whole of the power:
to stop, and stay, and stay.
"""


def main() -> int:
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        print(
            "error: poem must be 1-280 Unicode code points "
            "and not only whitespace",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
