# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1SecretVolumeSourceDict generated type."""
from typing import TypedDict, List

from .v1_key_to_path import V1KeyToPathDict

V1SecretVolumeSourceDict = TypedDict(
    "V1SecretVolumeSourceDict",
    {
        "defaultMode": int,
        "items": List[V1KeyToPathDict],
        "optional": bool,
        "secretName": str,
    },
    total=False,
)
