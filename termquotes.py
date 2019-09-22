#!/usr/bin/python

'''
A collection of programmer-focused quotes chosen at random.
'''

import random
import re
from typing import Dict, List

# Match more than 2+ spaces
space_pat = re.compile(r"[ ]{2,}")

quotes: List[Dict[str, str]] = [
    {
        "text": """
        Assumptions that aren't based on well-established facts
        are the bane of all projects.
        """,
        "source": "Pragmatic Programmer",
    },
    {
        "text": """
        It's easy to assume X causes Y - don't assume it, prove it.
        """,
        "source": "Pragmatic Programmer",
    },
]


def clean_text(text: str) -> str:
    return re.sub(space_pat, " ", text.strip()).replace("\n", "")


def attach_source(quote: str, source: str) -> str:
    return f"{quote}\n-- {source}"


clean_quotes: List[str] = [
    attach_source(clean_text(quote["text"]), quote["source"])
    for quote in quotes
]

chosen_quote: str = random.choice(clean_quotes)

print(chosen_quote)
