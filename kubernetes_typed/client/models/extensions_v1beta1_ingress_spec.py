# Code generated by `typeddictgen`. DO NOT EDIT.
"""ExtensionsV1beta1IngressSpecDict generated type."""
from typing import TypedDict, List

from .extensions_v1beta1_ingress_backend import ExtensionsV1beta1IngressBackendDict
from .extensions_v1beta1_ingress_rule import ExtensionsV1beta1IngressRuleDict
from .extensions_v1beta1_ingress_tls import ExtensionsV1beta1IngressTLSDict

ExtensionsV1beta1IngressSpecDict = TypedDict(
    "ExtensionsV1beta1IngressSpecDict",
    {
        "backend": ExtensionsV1beta1IngressBackendDict,
        "ingressClassName": str,
        "rules": List[ExtensionsV1beta1IngressRuleDict],
        "tls": List[ExtensionsV1beta1IngressTLSDict],
    },
    total=False,
)
