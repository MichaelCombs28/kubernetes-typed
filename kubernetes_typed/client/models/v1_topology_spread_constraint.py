# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TopologySpreadConstraintDict generated type."""
from typing import TypedDict

from .v1_label_selector import V1LabelSelectorDict

V1TopologySpreadConstraintDict = TypedDict(
    "V1TopologySpreadConstraintDict",
    {
        "labelSelector": V1LabelSelectorDict,
        "maxSkew": int,
        "topologyKey": str,
        "whenUnsatisfiable": str,
    },
    total=False,
)
