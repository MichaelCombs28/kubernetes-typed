# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CustomResourceConversionDict generated type."""
from typing import TypedDict

from .v1_webhook_conversion import V1WebhookConversionDict

V1CustomResourceConversionDict = TypedDict(
    "V1CustomResourceConversionDict",
    {
        "strategy": str,
        "webhook": V1WebhookConversionDict,
    },
    total=False,
)
