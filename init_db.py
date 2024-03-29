"""
DB Setup
"""

import datetime
import json
import os
import sqlite3

DB_NAME = "quotes.db"
SEEDS_DIR = "seeds"

create_sql: str = """
create table if not exists quotes (
    id integer primary key,
    text text unique,
    source text,
    topic text,
    created timestamp
)
"""
insert_sql: str = """
insert into quotes (text, source, topic, created) values (?, ?, ?, ?)
"""


def init_db():
    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()
    cur.execute(create_sql)

    conn.commit()

    print("Created DB")

    return conn


def load_seeds(conn):
    js = []

    now = datetime.datetime.now()

    for file_name in os.listdir(SEEDS_DIR):
        if not file_name.endswith(".json"):
            continue

        with open(os.path.join(SEEDS_DIR, file_name)) as f:
            js += json.loads(f.read())

    topic, _ = file_name.split(".")

    cur = conn.cursor()

    for quote in js:
        print(topic, quote)
        cur.execute(insert_sql, (quote["text"], quote["source"], topic, now))

    conn.commit()


if __name__ == "__main__":
    conn = init_db()

    print("Loading ...")
    load_seeds(conn)
    print("Done")
