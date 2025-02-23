# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1StorageClassDict generated type."""
from typing import TypedDict, Dict, List

from .v1_object_meta import V1ObjectMetaDict
from .v1_topology_selector_term import V1TopologySelectorTermDict

V1StorageClassDict = TypedDict(
    "V1StorageClassDict",
    {
        "allowVolumeExpansion": bool,
        "allowedTopologies": List[V1TopologySelectorTermDict],
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "mountOptions": List[str],
        "parameters": Dict[str, str],
        "provisioner": str,
        "reclaimPolicy": str,
        "volumeBindingMode": str,
    },
    total=False,
)
