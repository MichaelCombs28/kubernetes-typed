# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1IngressClassSpecDict generated type."""
from typing import TypedDict

from .v1_typed_local_object_reference import V1TypedLocalObjectReferenceDict

V1beta1IngressClassSpecDict = TypedDict(
    "V1beta1IngressClassSpecDict",
    {
        "controller": str,
        "parameters": V1TypedLocalObjectReferenceDict,
    },
    total=False,
)
