# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1LabelSelectorDict generated type."""
from typing import TypedDict, Dict, List

from .v1_label_selector_requirement import V1LabelSelectorRequirementDict

V1LabelSelectorDict = TypedDict(
    "V1LabelSelectorDict",
    {
        "matchExpressions": List[V1LabelSelectorRequirementDict],
        "matchLabels": Dict[str, str],
    },
    total=False,
)
