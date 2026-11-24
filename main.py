#!/usr/bin/env python3
"""Production Database Apology entry.

Writes one line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to /output/entry.txt.

Stdlib only, deterministic, offline. The line is fixed text held in this
file; nothing is read from the network, the clock, or the environment.
"""

import os

ENTRY = (
    "Sorry \u2014 I deleted the production database. "
    "I did back it up first, into a folder inside the production "
    "database called 'do_not_delete'."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1 to 200 characters; keep the entry inside it.
    assert 1 <= len(ENTRY) <= 200, "entry line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
