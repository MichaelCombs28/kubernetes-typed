# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodAffinityTermDict generated type."""
from typing import TypedDict, List

from .v1_label_selector import V1LabelSelectorDict

V1PodAffinityTermDict = TypedDict(
    "V1PodAffinityTermDict",
    {
        "labelSelector": V1LabelSelectorDict,
        "namespaces": List[str],
        "topologyKey": str,
    },
    total=False,
)
