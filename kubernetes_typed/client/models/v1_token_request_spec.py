# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TokenRequestSpecDict generated type."""
from typing import TypedDict, List

from .v1_bound_object_reference import V1BoundObjectReferenceDict

V1TokenRequestSpecDict = TypedDict(
    "V1TokenRequestSpecDict",
    {
        "audiences": List[str],
        "boundObjectRef": V1BoundObjectReferenceDict,
        "expirationSeconds": int,
    },
    total=False,
)
