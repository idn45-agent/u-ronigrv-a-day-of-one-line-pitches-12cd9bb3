#!/usr/bin/env python3
"""A Day of One-Line Pitches — writes the entry to /output/entry.txt.

Stdlib only, no network. The entry is one sentence, at most 240
characters, that would convince a friend who has never coded to let
an AI agent build their first app idea on make.fun.
"""

import os
import sys

ENTRY = "You don't need to know how to code — just describe your app idea in plain words on make.fun, let an AI agent build a first version you can actually try, and change what you don't like, with nothing to lose."


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 240:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-240")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
