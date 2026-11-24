#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (override the path with argv[1]).

Gate (kit RULES.txt): the file must be UTF-8 text of 1-120
characters and not only whitespace, or the entry is never judged.
"""

import os
import sys

TEXT = "Out of office. I've been ignored since March and I'm thriving on spite and tap water. Back when someone remembers me."

OUTPUT = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(TEXT) <= 120:
        raise SystemExit(f"entry is {len(TEXT)} chars, must be 1-120")
    if not TEXT.strip():
        raise SystemExit("entry must not be only whitespace")
    path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT
    folder = os.path.dirname(os.path.abspath(path))
    os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
