# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1PriorityClassListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1alpha1_priority_class import V1alpha1PriorityClassDict

V1alpha1PriorityClassListDict = TypedDict(
    "V1alpha1PriorityClassListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1PriorityClassDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
