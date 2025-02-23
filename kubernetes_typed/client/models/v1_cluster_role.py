# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ClusterRoleDict generated type."""
from typing import TypedDict, List

from .v1_aggregation_rule import V1AggregationRuleDict
from .v1_object_meta import V1ObjectMetaDict
from .v1_policy_rule import V1PolicyRuleDict

V1ClusterRoleDict = TypedDict(
    "V1ClusterRoleDict",
    {
        "aggregationRule": V1AggregationRuleDict,
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "rules": List[V1PolicyRuleDict],
    },
    total=False,
)
