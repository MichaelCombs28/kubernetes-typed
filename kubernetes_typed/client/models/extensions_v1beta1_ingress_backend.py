# Code generated by `typeddictgen`. DO NOT EDIT.
"""ExtensionsV1beta1IngressBackendDict generated type."""
from typing import TypedDict

from .v1_typed_local_object_reference import V1TypedLocalObjectReferenceDict

ExtensionsV1beta1IngressBackendDict = TypedDict(
    "ExtensionsV1beta1IngressBackendDict",
    {
        "resource": V1TypedLocalObjectReferenceDict,
        "serviceName": str,
        "servicePort": object,
    },
    total=False,
)
