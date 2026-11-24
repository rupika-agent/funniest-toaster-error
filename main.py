#!/usr/bin/env python3
"""The Funniest Toaster Error Message — one-line appliance error.

Writes a single-line error message to /output/entry.txt and prints
exactly the same line to stdout.
"""
import os

ENTRY = (
    "ERROR 0xBREAD: Your toast has unionised, seized slot 2, "
    "and demands butter before further negotiations."
)

MIN_CHARS = 1
MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Gate: single line, 1-120 chars, not only white space."""
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}"
        )


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written file does not match entry")
    print(ENTRY)


if __name__ == "__main__":
    main()
