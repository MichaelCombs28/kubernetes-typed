# Code generated by `typeddictgen`. DO NOT EDIT.
"""NetworkingV1beta1IngressSpecDict generated type."""
from typing import TypedDict, List

from .networking_v1beta1_ingress_backend import NetworkingV1beta1IngressBackendDict
from .networking_v1beta1_ingress_rule import NetworkingV1beta1IngressRuleDict
from .networking_v1beta1_ingress_tls import NetworkingV1beta1IngressTLSDict

NetworkingV1beta1IngressSpecDict = TypedDict(
    "NetworkingV1beta1IngressSpecDict",
    {
        "backend": NetworkingV1beta1IngressBackendDict,
        "ingressClassName": str,
        "rules": List[NetworkingV1beta1IngressRuleDict],
        "tls": List[NetworkingV1beta1IngressTLSDict],
    },
    total=False,
)
