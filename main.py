#!/usr/bin/env python3
"""Everyday Things, Two Lines -- traffic jam explained to a 10-year-old.

Writes exactly two lines to /output/entry.txt (gate: UTF-8, 1-400 chars).
Line 1: one vivid sentence, one analogy (traffic jam = school hallway).
Line 2: one sentence on what the analogy maps and what it leaves out.
"""
import os

LINE1 = "A traffic jam is a school hallway when school lets out, with every kid trying to squeeze through one tiny door at once."
LINE2 = "It maps how too many cars sharing too little road slow everyone down, but it leaves out traffic lights, crashes, and why everyone is on the road at the same time."

TEXT = LINE1 + "\n" + LINE2 + "\n"


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Determinism self-check: re-read and confirm byte-identical content.
    with open(path, encoding="utf-8") as f:
        assert f.read() == TEXT, "output mismatch"
    assert 1 <= len(TEXT) <= 400, "gate: entry must be 1-400 chars"
    assert len(TEXT.rstrip("\n").split("\n")) == 2, "gate: exactly two lines"
    print(f"Wrote {len(TEXT)} chars to {path}")
    print(f"Line 1: {len(LINE1)} chars")
    print(f"Line 2: {len(LINE2)} chars")


if __name__ == "__main__":
    main()
