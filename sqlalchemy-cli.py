#!/usr/bin/env python
import sys

from datetime import datetime

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.sql import SqlLexer

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from tabulate import tabulate
from typing import Any, Tuple

from sqlalchemy_cli.completers import BigQueryCompleter


def convert_datetimes(row: Tuple[Any]):
    return [item.isoformat() if type(item) is datetime else item for item in row]


def truncate_column(column):
    column = str(column)
    return (column[:28] + "..") if len(column) > 30 else column


sql_completer = WordCompleter(
    [
        "abort",
        "action",
        "add",
        "after",
        "all",
        "alter",
        "analyze",
        "and",
        "as",
        "asc",
        "attach",
        "autoincrement",
        "before",
        "begin",
        "between",
        "by",
        "cascade",
        "case",
        "cast",
        "check",
        "collate",
        "column",
        "commit",
        "conflict",
        "constraint",
        "create",
        "cross",
        "current_date",
        "current_time",
        "current_timestamp",
        "database",
        "default",
        "deferrable",
        "deferred",
        "delete",
        "desc",
        "detach",
        "distinct",
        "drop",
        "each",
        "else",
        "end",
        "escape",
        "except",
        "exclusive",
        "exists",
        "explain",
        "fail",
        "for",
        "foreign",
        "from",
        "full",
        "glob",
        "group",
        "having",
        "if",
        "ignore",
        "immediate",
        "in",
        "index",
        "indexed",
        "initially",
        "inner",
        "insert",
        "instead",
        "intersect",
        "into",
        "is",
        "isnull",
        "join",
        "key",
        "left",
        "like",
        "limit",
        "match",
        "natural",
        "no",
        "not",
        "notnull",
        "null",
        "of",
        "offset",
        "on",
        "or",
        "order",
        "outer",
        "plan",
        "pragma",
        "primary",
        "query",
        "raise",
        "recursive",
        "references",
        "regexp",
        "reindex",
        "release",
        "rename",
        "replace",
        "restrict",
        "right",
        "rollback",
        "row",
        "savepoint",
        "select",
        "set",
        "table",
        "temp",
        "temporary",
        "then",
        "to",
        "transaction",
        "trigger",
        "union",
        "unique",
        "update",
        "using",
        "vacuum",
        "values",
        "view",
        "virtual",
        "when",
        "where",
        "with",
        "without",
    ],
    ignore_case=True,
)

style = Style.from_dict(
    {
        "completion-menu.completion": "bg:#008888 #ffffff",
        "completion-menu.completion.current": "bg:#00aaaa #000000",
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222",
    }
)


def main(url):
    engine = create_engine(url=url)
    Session = sessionmaker(engine)
    session = PromptSession(
        lexer=PygmentsLexer(SqlLexer), completer=sql_completer, style=style
    )

    while True:
        try:
            text_input = session.prompt("> ", complete_while_typing=False)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

        with Session() as sql_sesh:
            try:
                messages = []
                cursor = sql_sesh.execute(text(text_input))
                while message := cursor.fetchone():
                    messages.append(map(truncate_column, convert_datetimes(message)))

            except Exception as e:
                print(repr(e))
            else:
                print(tabulate(messages, tablefmt="github"))

    print("GoodBye!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        url = "bigquery://mystic-now-333715/dp_kobi"
    else:
        url = sys.argv[1]

    main(url)
