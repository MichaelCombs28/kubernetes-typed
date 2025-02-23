# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CephFSVolumeSourceDict generated type."""
from typing import TypedDict, List

from .v1_local_object_reference import V1LocalObjectReferenceDict

V1CephFSVolumeSourceDict = TypedDict(
    "V1CephFSVolumeSourceDict",
    {
        "monitors": List[str],
        "path": str,
        "readOnly": bool,
        "secretFile": str,
        "secretRef": V1LocalObjectReferenceDict,
        "user": str,
    },
    total=False,
)
