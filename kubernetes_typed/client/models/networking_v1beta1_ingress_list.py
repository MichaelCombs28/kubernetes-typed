# Code generated by `typeddictgen`. DO NOT EDIT.
"""NetworkingV1beta1IngressListDict generated type."""
from typing import TypedDict, List

from .networking_v1beta1_ingress import NetworkingV1beta1IngressDict
from .v1_list_meta import V1ListMetaDict

NetworkingV1beta1IngressListDict = TypedDict(
    "NetworkingV1beta1IngressListDict",
    {
        "apiVersion": str,
        "items": List[NetworkingV1beta1IngressDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
