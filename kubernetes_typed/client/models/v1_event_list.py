# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1EventListDict generated type."""
from typing import TypedDict, List

from .v1_event import V1EventDict
from .v1_list_meta import V1ListMetaDict

V1EventListDict = TypedDict(
    "V1EventListDict",
    {
        "apiVersion": str,
        "items": List[V1EventDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
