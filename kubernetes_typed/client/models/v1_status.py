# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1StatusDict generated type."""
from typing import TypedDict

from .v1_list_meta import V1ListMetaDict
from .v1_status_details import V1StatusDetailsDict

V1StatusDict = TypedDict(
    "V1StatusDict",
    {
        "apiVersion": str,
        "code": int,
        "details": V1StatusDetailsDict,
        "kind": str,
        "message": str,
        "metadata": V1ListMetaDict,
        "reason": str,
        "status": str,
    },
    total=False,
)
