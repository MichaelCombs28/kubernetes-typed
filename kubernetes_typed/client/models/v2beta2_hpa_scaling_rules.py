# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2HPAScalingRulesDict generated type."""
from typing import TypedDict, List

from .v2beta2_hpa_scaling_policy import V2beta2HPAScalingPolicyDict

V2beta2HPAScalingRulesDict = TypedDict(
    "V2beta2HPAScalingRulesDict",
    {
        "policies": List[V2beta2HPAScalingPolicyDict],
        "selectPolicy": str,
        "stabilizationWindowSeconds": int,
    },
    total=False,
)
