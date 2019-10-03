#!/usr/bin/python

"""
A collection of programmer-focused quotes chosen at random.
"""

import os
import sqlite3
from pathlib import Path

import click
from termquotes import __version__
from termquotes.api import (add_quote, get_quote_by_id, get_random_quote,
                            list_quotes)


class TermQuotesConf:
    def __init__(self, db_path):
        self.project_path = Path(__file__).parent
        self.db_path = os.path.join(self.project_path, db_path)

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        self.db = conn


@click.group()
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, db_path="data/quotes.db") -> None:
    """
    A little CLI tool to record, categorize and display quotes
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
@click.pass_obj
def add(conf) -> None:
    quote: str = click.prompt(click.style("Quote", fg="green"))
    source: str = click.prompt(click.style("Source", fg="green"))

    created, err = add_quote(conn=conf.db, text=quote, source=source)

    if created:
        click.secho(f"Added quote ID: {created}", fg="green")

    else:
        click.secho(f"Could not add quote: {err}", fg="red")


@click.command(help="Lists quotes")
@click.pass_obj
def ls(conf) -> None:

    quotes = list_quotes(conn=conf.db)

    if not quotes:
        click.secho(f"No quotes found :(", fg="yellow")

        return

    for quote in quotes:
        id_part = click.style(f"[{quote['id']}]", bold=True, fg="white")
        rest = click.style(f"{quote['text']} -- {quote['source']}", fg="green")
        click.echo(f"{id_part} {rest}")
        click.secho("-" * 50, fg="blue")


cli.add_command(ls)
cli.add_command(get)
cli.add_command(add)

if __name__ == "__main__":
    cli()
