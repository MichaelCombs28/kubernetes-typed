# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CustomResourceSubresourcesDict generated type."""
from typing import TypedDict

from .v1_custom_resource_subresource_scale import V1CustomResourceSubresourceScaleDict

V1CustomResourceSubresourcesDict = TypedDict(
    "V1CustomResourceSubresourcesDict",
    {
        "scale": V1CustomResourceSubresourceScaleDict,
        "status": object,
    },
    total=False,
)
