# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CustomResourceValidationDict generated type."""
from typing import TypedDict

from .v1_json_schema_props import V1JSONSchemaPropsDict

V1CustomResourceValidationDict = TypedDict(
    "V1CustomResourceValidationDict",
    {
        "openAPIV3Schema": V1JSONSchemaPropsDict,
    },
    total=False,
)
