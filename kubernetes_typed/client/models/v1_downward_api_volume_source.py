# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1DownwardAPIVolumeSourceDict generated type."""
from typing import TypedDict, List

from .v1_downward_api_volume_file import V1DownwardAPIVolumeFileDict

V1DownwardAPIVolumeSourceDict = TypedDict(
    "V1DownwardAPIVolumeSourceDict",
    {
        "defaultMode": int,
        "items": List[V1DownwardAPIVolumeFileDict],
    },
    total=False,
)
