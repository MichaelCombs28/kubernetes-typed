# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CSINodeDriverDict generated type."""
from typing import TypedDict, List

from .v1beta1_volume_node_resources import V1beta1VolumeNodeResourcesDict

V1beta1CSINodeDriverDict = TypedDict(
    "V1beta1CSINodeDriverDict",
    {
        "allocatable": V1beta1VolumeNodeResourcesDict,
        "name": str,
        "nodeID": str,
        "topologyKeys": List[str],
    },
    total=False,
)
