# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CustomResourceDefinitionSpecDict generated type."""
from typing import TypedDict, List

from .v1_custom_resource_conversion import V1CustomResourceConversionDict
from .v1_custom_resource_definition_names import V1CustomResourceDefinitionNamesDict
from .v1_custom_resource_definition_version import V1CustomResourceDefinitionVersionDict

V1CustomResourceDefinitionSpecDict = TypedDict(
    "V1CustomResourceDefinitionSpecDict",
    {
        "conversion": V1CustomResourceConversionDict,
        "group": str,
        "names": V1CustomResourceDefinitionNamesDict,
        "preserveUnknownFields": bool,
        "scope": str,
        "versions": List[V1CustomResourceDefinitionVersionDict],
    },
    total=False,
)
