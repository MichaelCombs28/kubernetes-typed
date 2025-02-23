# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1SubjectRulesReviewStatusDict generated type."""
from typing import TypedDict, List

from .v1beta1_non_resource_rule import V1beta1NonResourceRuleDict
from .v1beta1_resource_rule import V1beta1ResourceRuleDict

V1beta1SubjectRulesReviewStatusDict = TypedDict(
    "V1beta1SubjectRulesReviewStatusDict",
    {
        "evaluationError": str,
        "incomplete": bool,
        "nonResourceRules": List[V1beta1NonResourceRuleDict],
        "resourceRules": List[V1beta1ResourceRuleDict],
    },
    total=False,
)
