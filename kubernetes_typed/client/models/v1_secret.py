# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1SecretDict generated type."""
from typing import TypedDict, Dict

from .v1_object_meta import V1ObjectMetaDict

V1SecretDict = TypedDict(
    "V1SecretDict",
    {
        "apiVersion": str,
        "data": Dict[str, str],
        "immutable": bool,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "stringData": Dict[str, str],
        "type": str,
    },
    total=False,
)
