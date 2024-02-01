# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1AffinityDict generated type."""
from typing import TypedDict

from .v1_node_affinity import V1NodeAffinityDict
from .v1_pod_affinity import V1PodAffinityDict
from .v1_pod_anti_affinity import V1PodAntiAffinityDict

V1AffinityDict = TypedDict(
    "V1AffinityDict",
    {
        "nodeAffinity": V1NodeAffinityDict,
        "podAffinity": V1PodAffinityDict,
        "podAntiAffinity": V1PodAntiAffinityDict,
    },
    total=False,
)
