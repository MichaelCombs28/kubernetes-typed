# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TokenRequestDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1_token_request_spec import V1TokenRequestSpecDict
from .v1_token_request_status import V1TokenRequestStatusDict

V1TokenRequestDict = TypedDict(
    "V1TokenRequestDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1TokenRequestSpecDict,
        "status": V1TokenRequestStatusDict,
    },
    total=False,
)
