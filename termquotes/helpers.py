"""
Various utilities and helpers
"""

import re

# Match more than 2+ spaces
space_pat = re.compile(r"[ ]{2,}")


def clean_text(text: str) -> str:
    return re.sub(space_pat, " ", text.strip()).replace("\n", "")
