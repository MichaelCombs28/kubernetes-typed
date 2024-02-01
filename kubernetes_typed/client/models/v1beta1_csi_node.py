# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CSINodeDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1beta1_csi_node_spec import V1beta1CSINodeSpecDict

V1beta1CSINodeDict = TypedDict(
    "V1beta1CSINodeDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1CSINodeSpecDict,
    },
    total=False,
)
