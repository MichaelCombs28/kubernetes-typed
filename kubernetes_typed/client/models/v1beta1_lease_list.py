# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1LeaseListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1beta1_lease import V1beta1LeaseDict

V1beta1LeaseListDict = TypedDict(
    "V1beta1LeaseListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1LeaseDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
