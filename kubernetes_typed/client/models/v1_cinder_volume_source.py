# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CinderVolumeSourceDict generated type."""
from typing import TypedDict

from .v1_local_object_reference import V1LocalObjectReferenceDict

V1CinderVolumeSourceDict = TypedDict(
    "V1CinderVolumeSourceDict",
    {
        "fsType": str,
        "readOnly": bool,
        "secretRef": V1LocalObjectReferenceDict,
        "volumeID": str,
    },
    total=False,
)
