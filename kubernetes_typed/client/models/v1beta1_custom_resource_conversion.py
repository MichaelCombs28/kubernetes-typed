# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CustomResourceConversionDict generated type."""
from typing import TypedDict, List

from .apiextensions_v1beta1_webhook_client_config import ApiextensionsV1beta1WebhookClientConfigDict

V1beta1CustomResourceConversionDict = TypedDict(
    "V1beta1CustomResourceConversionDict",
    {
        "conversionReviewVersions": List[str],
        "strategy": str,
        "webhookClientConfig": ApiextensionsV1beta1WebhookClientConfigDict,
    },
    total=False,
)
