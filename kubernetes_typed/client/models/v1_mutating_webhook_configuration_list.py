# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1MutatingWebhookConfigurationListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1_mutating_webhook_configuration import V1MutatingWebhookConfigurationDict

V1MutatingWebhookConfigurationListDict = TypedDict(
    "V1MutatingWebhookConfigurationListDict",
    {
        "apiVersion": str,
        "items": List[V1MutatingWebhookConfigurationDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
