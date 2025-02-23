# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1MutatingWebhookDict generated type."""
from typing import TypedDict, List

from .admissionregistration_v1_webhook_client_config import AdmissionregistrationV1WebhookClientConfigDict
from .v1_label_selector import V1LabelSelectorDict
from .v1_rule_with_operations import V1RuleWithOperationsDict

V1MutatingWebhookDict = TypedDict(
    "V1MutatingWebhookDict",
    {
        "admissionReviewVersions": List[str],
        "clientConfig": AdmissionregistrationV1WebhookClientConfigDict,
        "failurePolicy": str,
        "matchPolicy": str,
        "name": str,
        "namespaceSelector": V1LabelSelectorDict,
        "objectSelector": V1LabelSelectorDict,
        "reinvocationPolicy": str,
        "rules": List[V1RuleWithOperationsDict],
        "sideEffects": str,
        "timeoutSeconds": int,
    },
    total=False,
)
