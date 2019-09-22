#!/usr/bin/python

"""
A collection of programmer-focused quotes chosen at random.
"""

import random
import re
from typing import Dict, List

# Match more than 2+ spaces
space_pat = re.compile(r"[ ]{2,}")


def clean_text(text: str) -> str:
    return re.sub(space_pat, " ", text.strip()).replace("\n", "")


def attach_source(quote: str, source: str) -> str:
    return f"{quote}\n-- {source}"


quotes: List[Dict[str, str]] = [
    {
        "text": "Simplicity is prerequisite for reliability.",
        "source": "Edsger W. Dijkstra",
    },
    {
        "text": "There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies. The first method is far more difficult.",
        "source": "C. A. R Hoare",
    },
    {
        "text": "Readability is essential for maintainability.",
        "source": "Mark Reinhold (JVM Language Summit 2018)",
    },
    {
        "text": "Programs must be written for people to read, and only incidentally for machines to execute.",
        "source": "Hal Abelson and Gerald Sussman (SICP)",
    },
    {
        "text": "The most important skill for a programmer is the ability to effectively communicate ideas.",
        "source": "Gastón Jorquera",
    },
    {
        "text": "Design is the art of arranging code to work today, and be changeable forever.",
        "source": "Sandi Metz",
    },
    {
        "text": "Poor naming is symptomatic of poor design.",
        "source": "Dave Cheney",
    },
    {
        "text": "Good code has lots of comments, bad code requires lots of comments.",
        "source": "Dave Thomas and Andrew Hunt (Pragmatic Programmer)",
    },
    {
        "text": "Don’t comment bad code — rewrite it",
        "source": "Brian Kernighan",
    },
    {
        "text": "APIs should be easy to use and hard to misuse.",
        "source": "Josh Bloch",
    },
    {
        "text": "What matters for simplicity is that there's not interleaving.",
        "source": "Rich Hickey",
    },
    {
        "text": "Simplicity is hard work. But, there's a huge payoff. The person who has a genuinely simpler system - a system made out of genuinely simple parts, is going to be able to affect the greatest change with the least work. He's going to kick your ass. He's gonna spend more time simplifying things up front and in the long haul he's gonna wipe the plate with you because he'll have that ability to change things when you're struggling to push elephants around.",
        "source": "Rich Hickey",
    },
    {
        "text": "Controlling complexity is the essence of computer programming.",
        "source": "Brian Kernighan",
    },
    {
        "text": "Assumptions that aren't based on well-established facts are the bane of all projects.",
        "source": "Dave Thomas and Andrew Hunt (Pragmatic Programmer)",
    },
    {
        "text": "It's easy to assume X causes Y - don't assume it, prove it.",
        "source": "Dave Thomas and Andrew Hunt (Pragmatic Programmer)",
    },
    {
        "text": "Don't be a slave to history. Don't let existing code dictate future code. All code can be replaced if it is not longer appropriate.  This decision may impact the project schedule. The assumption is that the impact will be less than the cost of NOT making the change.",
        "source": "Dave Thomas and Andrew Hunt (Pragmatic Programmer)",
    },
]

clean_quotes: List[str] = [
    attach_source(clean_text(quote["text"]), quote["source"])
    for quote in quotes
]

chosen_quote: str = random.choice(clean_quotes)

print(chosen_quote)
