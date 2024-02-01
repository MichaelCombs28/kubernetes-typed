# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1_pod_spec import V1PodSpecDict
from .v1_pod_status import V1PodStatusDict

V1PodDict = TypedDict(
    "V1PodDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1PodSpecDict,
        "status": V1PodStatusDict,
    },
    total=False,
)
