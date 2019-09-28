"""
Various utilities and helpers
"""

import re
from typing import Tuple

# Match more than 2+ spaces
space_pat = re.compile(r"[ ]{2,}")


def clean_text(text: str) -> str:
    return re.sub(space_pat, " ", text.strip()).replace("\n", "")


def attach_source(quote: str, source: str) -> str:
    return f"{quote}\n-- {source}"


def select_random(conn) -> Tuple[str, str]:
    """
    Selects a random quote
    """

    cur = conn.cursor()

    cur.execute("select text, source from quotes order by random() limit 1")

    text, source = cur.fetchone()

    return text, source
