# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1DownwardAPIVolumeFileDict generated type."""
from typing import TypedDict

from .v1_object_field_selector import V1ObjectFieldSelectorDict
from .v1_resource_field_selector import V1ResourceFieldSelectorDict

V1DownwardAPIVolumeFileDict = TypedDict(
    "V1DownwardAPIVolumeFileDict",
    {
        "fieldRef": V1ObjectFieldSelectorDict,
        "mode": int,
        "path": str,
        "resourceFieldRef": V1ResourceFieldSelectorDict,
    },
    total=False,
)
