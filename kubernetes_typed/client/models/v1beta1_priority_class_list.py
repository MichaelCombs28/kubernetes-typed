# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PriorityClassListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1beta1_priority_class import V1beta1PriorityClassDict

V1beta1PriorityClassListDict = TypedDict(
    "V1beta1PriorityClassListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1PriorityClassDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
