# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1ValidatingWebhookConfigurationDict generated type."""
from typing import TypedDict, List

from .v1_object_meta import V1ObjectMetaDict
from .v1beta1_validating_webhook import V1beta1ValidatingWebhookDict

V1beta1ValidatingWebhookConfigurationDict = TypedDict(
    "V1beta1ValidatingWebhookConfigurationDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "webhooks": List[V1beta1ValidatingWebhookDict],
    },
    total=False,
)
