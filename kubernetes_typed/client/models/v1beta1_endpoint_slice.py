# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1EndpointSliceDict generated type."""
from typing import TypedDict, List

from .v1_object_meta import V1ObjectMetaDict
from .v1beta1_endpoint import V1beta1EndpointDict
from .v1beta1_endpoint_port import V1beta1EndpointPortDict

V1beta1EndpointSliceDict = TypedDict(
    "V1beta1EndpointSliceDict",
    {
        "addressType": str,
        "apiVersion": str,
        "endpoints": List[V1beta1EndpointDict],
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "ports": List[V1beta1EndpointPortDict],
    },
    total=False,
)
