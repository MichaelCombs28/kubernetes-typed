# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1LoadBalancerStatusDict generated type."""
from typing import TypedDict, List

from .v1_load_balancer_ingress import V1LoadBalancerIngressDict

V1LoadBalancerStatusDict = TypedDict(
    "V1LoadBalancerStatusDict",
    {
        "ingress": List[V1LoadBalancerIngressDict],
    },
    total=False,
)
