# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CSINodeListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1beta1_csi_node import V1beta1CSINodeDict

V1beta1CSINodeListDict = TypedDict(
    "V1beta1CSINodeListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1CSINodeDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
