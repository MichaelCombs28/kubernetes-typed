# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1StatusDetailsDict generated type."""
from typing import TypedDict, List

from .v1_status_cause import V1StatusCauseDict

V1StatusDetailsDict = TypedDict(
    "V1StatusDetailsDict",
    {
        "causes": List[V1StatusCauseDict],
        "group": str,
        "kind": str,
        "name": str,
        "retryAfterSeconds": int,
        "uid": str,
    },
    total=False,
)
