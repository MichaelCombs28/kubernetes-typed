# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ServiceSpecDict generated type."""
from typing import TypedDict, Dict, List

from .v1_service_port import V1ServicePortDict
from .v1_session_affinity_config import V1SessionAffinityConfigDict

V1ServiceSpecDict = TypedDict(
    "V1ServiceSpecDict",
    {
        "clusterIP": str,
        "externalIPs": List[str],
        "externalName": str,
        "externalTrafficPolicy": str,
        "healthCheckNodePort": int,
        "ipFamily": str,
        "loadBalancerIP": str,
        "loadBalancerSourceRanges": List[str],
        "ports": List[V1ServicePortDict],
        "publishNotReadyAddresses": bool,
        "selector": Dict[str, str],
        "sessionAffinity": str,
        "sessionAffinityConfig": V1SessionAffinityConfigDict,
        "topologyKeys": List[str],
        "type": str,
    },
    total=False,
)
