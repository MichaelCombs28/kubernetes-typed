# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1BindingDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1_object_reference import V1ObjectReferenceDict

V1BindingDict = TypedDict(
    "V1BindingDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "target": V1ObjectReferenceDict,
    },
    total=False,
)
