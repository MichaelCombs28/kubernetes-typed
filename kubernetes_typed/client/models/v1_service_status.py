# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ServiceStatusDict generated type."""
from typing import TypedDict

from .v1_load_balancer_status import V1LoadBalancerStatusDict

V1ServiceStatusDict = TypedDict(
    "V1ServiceStatusDict",
    {
        "loadBalancer": V1LoadBalancerStatusDict,
    },
    total=False,
)
