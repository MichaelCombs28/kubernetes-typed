# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1SupplementalGroupsStrategyOptionsDict generated type."""
from typing import TypedDict, List

from .v1beta1_id_range import V1beta1IDRangeDict

V1beta1SupplementalGroupsStrategyOptionsDict = TypedDict(
    "V1beta1SupplementalGroupsStrategyOptionsDict",
    {
        "ranges": List[V1beta1IDRangeDict],
        "rule": str,
    },
    total=False,
)
