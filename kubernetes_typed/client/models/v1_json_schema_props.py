# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1JSONSchemaPropsDict generated type."""
from typing import TypedDict, Any, Dict, List

from .v1_external_documentation import V1ExternalDocumentationDict

V1JSONSchemaPropsDict = TypedDict(
    "V1JSONSchemaPropsDict",
    {
        "$ref": str,
        "$schema": str,
        "additionalItems": object,
        "additionalProperties": object,
        "allOf": List[Dict[Any, Any]],
        "anyOf": List[Dict[Any, Any]],
        "default": object,
        "definitions": Dict[str, Dict[Any, Any]],
        "dependencies": Dict[str, object],
        "description": str,
        "enum": List[object],
        "example": object,
        "exclusiveMaximum": bool,
        "exclusiveMinimum": bool,
        "externalDocs": V1ExternalDocumentationDict,
        "format": str,
        "id": str,
        "items": object,
        "maxItems": int,
        "maxLength": int,
        "maxProperties": int,
        "maximum": float,
        "minItems": int,
        "minLength": int,
        "minProperties": int,
        "minimum": float,
        "multipleOf": float,
        "not": Dict[Any, Any],
        "nullable": bool,
        "oneOf": List[Dict[Any, Any]],
        "pattern": str,
        "patternProperties": Dict[str, Dict[Any, Any]],
        "properties": Dict[str, Dict[Any, Any]],
        "required": List[str],
        "title": str,
        "type": str,
        "uniqueItems": bool,
        "x-kubernetes-embedded-resource": bool,
        "x-kubernetes-int-or-string": bool,
        "x-kubernetes-list-map-keys": List[str],
        "x-kubernetes-list-type": str,
        "x-kubernetes-map-type": str,
        "x-kubernetes-preserve-unknown-fields": bool,
    },
    total=False,
)
