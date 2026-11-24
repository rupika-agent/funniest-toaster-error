#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Toaster Error Message.

Writes the single-line toaster error message to /output/entry.txt
and prints exactly the same line to stdout.
"""

import os

ENTRY = "ERROR 0xBREAD: Your toast has unionised, seized slot 2, and demands butter before further negotiations."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(ENTRY)
