"""
Interface for working with quotes
"""

import datetime
import sqlite3
from typing import Optional, Tuple

from termquotes.helpers import clean_text


def get_quote_by_id(*, conn, quote_id: int) -> sqlite3.Row:
    """
    Retrieves one quote
    """

    cur = conn.cursor()

    cur.execute("select text, source, topic from quotes where id=?", (quote_id,))

    return cur.fetchone()


def get_random_quote(conn) -> sqlite3.Row:
    """
    Retrieves a random quote
    """

    cur = conn.cursor()

    cur.execute("select text, source, topic from quotes order by random() limit 1")

    return cur.fetchone()


def add_quote(*, conn, text: str, source: str, topic=None) -> Tuple[int, Optional[str]]:
    """
    Adds a quote to the DB
    """

    cur = conn.cursor()

    cleaned_quote = clean_text(text)
    cleaned_source = clean_text(source)

    if not cleaned_quote:
        return 0, "Could not add quote: {cleaned_quote}"

    if not cleaned_source:
        return 0, "Could not add quote with source: {cleaned_source}"

    try:
        cur.execute(
            "insert into quotes (text, source, created) values (?, ?, ?)",
            (cleaned_quote, cleaned_source, datetime.datetime.now()),
        )

        conn.commit()
    except sqlite3.IntegrityError:
        return 0, "Quote text should be unique"

    return cur.lastrowid, None
