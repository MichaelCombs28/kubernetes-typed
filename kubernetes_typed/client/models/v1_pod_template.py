# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodTemplateDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1_pod_template_spec import V1PodTemplateSpecDict

V1PodTemplateDict = TypedDict(
    "V1PodTemplateDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "template": V1PodTemplateSpecDict,
    },
    total=False,
)
