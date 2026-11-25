#!/usr/bin/env python3
"""Fridge Roast entry: write one roast line to /output/entry.txt.

The line is a one-line roast of a smart fridge, chosen by manual ranking
against the competition's judge brief (roast the fridge itself, punchline
lands, fridge-specific, tight wording, fresh angle). See candidates.md
for the full candidate list and the ranking.
"""

import os

LINE = "My smart fridge has a password. I forgot the password. I am now locked out of my own leftovers."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
