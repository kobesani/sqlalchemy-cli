import logging

from collections import Counter
from re import compile
from typing import Iterable

from prompt_toolkit.completion import Completer, Completion, CompleteEvent
from prompt_toolkit.document import Document

_logger = logging.getLogger(__name__)


class BigQueryCompleter(Completer):
    keywords = [
        "ABORT",
        "ACTION",
        "ADD",
        "AFTER",
        "ALL",
        "ALTER",
        "ANALYZE",
        "AND",
        "AS",
        "ASC",
        "ATTACH",
        "AUTOINCREMENT",
        "BEFORE",
        "BEGIN",
        "BETWEEN",
        "BIGINT",
        "BLOB",
        "BOOLEAN",
        "BY",
        "CASCADE",
        "CASE",
        "CAST",
        "CHARACTER",
        "CHECK",
        "CLOB",
        "COLLATE",
        "COLUMN",
        "COMMIT",
        "CONFLICT",
        "CONSTRAINT",
        "CREATE",
        "CROSS",
        "CURRENT",
        "CURRENT_DATE",
        "CURRENT_TIME",
        "CURRENT_TIMESTAMP",
        "DATABASE",
        "DATE",
        "DATETIME",
        "DECIMAL",
        "DEFAULT",
        "DEFERRABLE",
        "DEFERRED",
        "DELETE",
        "DETACH",
        "DISTINCT",
        "DO",
        "DOUBLE PRECISION",
        "DOUBLE",
        "DROP",
        "EACH",
        "ELSE",
        "END",
        "ESCAPE",
        "EXCEPT",
        "EXCLUSIVE",
        "EXISTS",
        "EXPLAIN",
        "FAIL",
        "FILTER",
        "FLOAT",
        "FOLLOWING",
        "FOR",
        "FOREIGN",
        "FROM",
        "FULL",
        "GLOB",
        "GROUP",
        "HAVING",
        "IF",
        "IGNORE",
        "IMMEDIATE",
        "IN",
        "INDEX",
        "INDEXED",
        "INITIALLY",
        "INNER",
        "INSERT",
        "INSTEAD",
        "INT",
        "INT2",
        "INT8",
        "INTEGER",
        "INTERSECT",
        "INTO",
        "IS",
        "ISNULL",
        "JOIN",
        "KEY",
        "LEFT",
        "LIKE",
        "LIMIT",
        "MATCH",
        "MEDIUMINT",
        "NATIVE CHARACTER",
        "NATURAL",
        "NCHAR",
        "NO",
        "NOT",
        "NOTHING",
        "NULL",
        "NULLS FIRST",
        "NULLS LAST",
        "NUMERIC",
        "NVARCHAR",
        "OF",
        "OFFSET",
        "ON",
        "OR",
        "ORDER BY",
        "OUTER",
        "OVER",
        "PARTITION",
        "PLAN",
        "PRAGMA",
        "PRECEDING",
        "PRIMARY",
        "QUERY",
        "RAISE",
        "RANGE",
        "REAL",
        "RECURSIVE",
        "REFERENCES",
        "REGEXP",
        "REINDEX",
        "RELEASE",
        "RENAME",
        "REPLACE",
        "RESTRICT",
        "RIGHT",
        "ROLLBACK",
        "ROW",
        "ROWS",
        "SAVEPOINT",
        "SELECT",
        "SET",
        "SMALLINT",
        "TABLE",
        "TEMP",
        "TEMPORARY",
        "TEXT",
        "THEN",
        "TINYINT",
        "TO",
        "TRANSACTION",
        "TRIGGER",
        "UNBOUNDED",
        "UNION",
        "UNIQUE",
        "UNSIGNED BIG INT",
        "UPDATE",
        "USING",
        "VACUUM",
        "VALUES",
        "VARCHAR",
        "VARYING CHARACTER",
        "VIEW",
        "VIRTUAL",
        "WHEN",
        "WHERE",
        "WINDOW",
        "WITH",
        "WITHOUT",
    ]

    functions = [
        "ABS",
        "AVG",
        "CHANGES",
        "CHAR",
        "COALESCE",
        "COUNT",
        "CUME_DIST",
        "DATE",
        "DATETIME",
        "DENSE_RANK",
        "GLOB",
        "GROUP_CONCAT",
        "HEX",
        "IFNULL",
        "INSTR",
        "JSON",
        "JSON_ARRAY",
        "JSON_ARRAY_LENGTH",
        "JSON_EACH",
        "JSON_EXTRACT",
        "JSON_GROUP_ARRAY",
        "JSON_GROUP_OBJECT",
        "JSON_INSERT",
        "JSON_OBJECT",
        "JSON_PATCH",
        "JSON_QUOTE",
        "JSON_REMOVE",
        "JSON_REPLACE",
        "JSON_SET",
        "JSON_TREE",
        "JSON_TYPE",
        "JSON_VALID",
        "JULIANDAY",
        "LAG",
        "LAST_INSERT_ROWID",
        "LENGTH",
        "LIKELIHOOD",
        "LIKELY",
        "LOAD_EXTENSION",
        "LOWER",
        "LTRIM",
        "MAX",
        "MIN",
        "NTILE",
        "NULLIF",
        "PERCENT_RANK",
        "PRINTF",
        "QUOTE",
        "RANDOM",
        "RANDOMBLOB",
        "RANK",
        "REPLACE",
        "ROUND",
        "ROW_NUMBER",
        "RTRIM",
        "SOUNDEX",
        "SQLITE_COMPILEOPTION_GET",
        "SQLITE_COMPILEOPTION_USED",
        "SQLITE_OFFSET",
        "SQLITE_SOURCE_ID",
        "SQLITE_VERSION",
        "STRFTIME",
        "SUBSTR",
        "SUM",
        "TIME",
        "TOTAL",
        "TOTAL_CHANGES",
        "TRIM",
    ]

    def __init__(self, supported_formats=(), keyword_casing="auto"):

        super(self.__class__, self).__init__()
        self.reserved_words = set()
        for x in self.keywords:
            self.reserved_words.update(x.split())
        self.name_pattern = compile("^[_a-z][_a-z0-9\$]*$")

        self.special_commands = []
        self.table_formats = supported_formats
        if keyword_casing not in ("upper", "lower", "auto"):
            keyword_casing = "auto"
        self.keyword_casing = keyword_casing

    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]:
        while True:
            yield "blah"
