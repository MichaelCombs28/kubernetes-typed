# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1APIServiceListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1beta1_api_service import V1beta1APIServiceDict

V1beta1APIServiceListDict = TypedDict(
    "V1beta1APIServiceListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1APIServiceDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
