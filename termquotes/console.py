#!/usr/bin/python

"""
A collection of programmer-focused quotes chosen at random.
"""

import os
import sqlite3
from pathlib import Path

import click

from termquotes.helpers import select_random


class TermQuotesConf:
    def __init__(self, db_path):
        self.project_path = Path(__file__).parent
        self.db_path = os.path.join(self.project_path, db_path)
        self.db = sqlite3.connect(self.db_path)


@click.group()
@click.pass_context
def cli(ctx, db_path="data/quotes.db") -> None:
    """
    Quips of wisdom for the terminal
    """

    ctx.obj = TermQuotesConf(db_path=db_path)


@click.command(help="Retrieves one random quote")
@click.pass_obj
def get(conf) -> None:

    text, source = select_random(conf.db)
    full = f"{text} -- {source}"

    click.secho(full, fg="green")


@click.command(help="Adds a quote to the DB")
@click.option("--quote", prompt=True)
@click.pass_obj
def add(conf, quote: str) -> None:
    source = click.prompt("Source")

    click.echo(quote)
    click.echo(source)


cli.add_command(get)
cli.add_command(add)

if __name__ == "__main__":
    cli()
