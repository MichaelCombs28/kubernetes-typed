# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ControllerRevisionListDict generated type."""
from typing import TypedDict, List

from .v1_controller_revision import V1ControllerRevisionDict
from .v1_list_meta import V1ListMetaDict

V1ControllerRevisionListDict = TypedDict(
    "V1ControllerRevisionListDict",
    {
        "apiVersion": str,
        "items": List[V1ControllerRevisionDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
