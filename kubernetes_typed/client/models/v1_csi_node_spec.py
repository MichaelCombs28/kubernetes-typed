# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CSINodeSpecDict generated type."""
from typing import TypedDict, List

from .v1_csi_node_driver import V1CSINodeDriverDict

V1CSINodeSpecDict = TypedDict(
    "V1CSINodeSpecDict",
    {
        "drivers": List[V1CSINodeDriverDict],
    },
    total=False,
)
