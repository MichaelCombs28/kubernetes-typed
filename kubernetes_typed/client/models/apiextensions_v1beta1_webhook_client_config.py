# Code generated by `typeddictgen`. DO NOT EDIT.
"""ApiextensionsV1beta1WebhookClientConfigDict generated type."""
from typing import TypedDict

from .apiextensions_v1beta1_service_reference import ApiextensionsV1beta1ServiceReferenceDict

ApiextensionsV1beta1WebhookClientConfigDict = TypedDict(
    "ApiextensionsV1beta1WebhookClientConfigDict",
    {
        "caBundle": str,
        "service": ApiextensionsV1beta1ServiceReferenceDict,
        "url": str,
    },
    total=False,
)
