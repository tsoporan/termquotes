#!/usr/bin/python

"""
A collection of programmer-focused quotes chosen at random.
"""

import os
import sqlite3
from pathlib import Path

import click
from termquotes.api import add_quote, get_quote_by_id, get_random_quote


class TermQuotesConf:
    def __init__(self, db_path):
        self.project_path = Path(__file__).parent
        self.db_path = os.path.join(self.project_path, db_path)

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        self.db = conn


@click.group()
@click.pass_context
def cli(ctx, db_path="data/quotes.db") -> None:
    """
    Quips of wisdom for the terminal
    """

    ctx.obj = TermQuotesConf(db_path=db_path)


@click.command(help="Retrieves one random quote")
@click.argument("quote-id", required=False, type=int)
@click.pass_obj
def get(conf, quote_id) -> None:

    if quote_id:
        quote = get_quote_by_id(conn=conf.db, quote_id=quote_id)

    else:
        quote = get_random_quote(conn=conf.db)

    if not quote:
        click.secho(f"No quote found", fg="yellow")

        return

    full = f"{quote['text']} -- {quote['source']}"

    click.secho(full, fg="green")


@click.command(help="Adds a quote to the DB")
@click.option("--quote", prompt=True)
@click.pass_obj
def add(conf, quote: str) -> None:
    source: str = click.prompt("Source")

    created, err = add_quote(conn=conf.db, text=quote, source=source)

    if created:
        click.secho(f"Added quote ID: {created}", fg="green")

    else:
        click.secho(f"Could not add quote: {err}", fg="red")


cli.add_command(get)
cli.add_command(add)

if __name__ == "__main__":
    cli()
