# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PriorityClassDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict

V1beta1PriorityClassDict = TypedDict(
    "V1beta1PriorityClassDict",
    {
        "apiVersion": str,
        "description": str,
        "globalDefault": bool,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "preemptionPolicy": str,
        "value": int,
    },
    total=False,
)
