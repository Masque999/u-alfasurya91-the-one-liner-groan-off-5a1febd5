#!/usr/bin/env python3
"""The One-Liner Groan-Off — one original dad joke, up to 140 characters.

Writes the entry to /output/entry.txt for make.fun's program/v1 harness.
"""
import os

SENTENCE = "I asked the cloud for rain and it gave me a 400-page invoice — turns out 'the cloud' is just someone else's expensive computer."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    # Write-back verification: a silent bad write must fail loudly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != SENTENCE:
        raise SystemExit(f"entry mismatch: wrote {len(SENTENCE)} chars, read back {len(written)}")


if __name__ == "__main__":
    main()
