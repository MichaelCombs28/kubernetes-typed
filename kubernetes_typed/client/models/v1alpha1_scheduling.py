# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1SchedulingDict generated type."""
from typing import TypedDict, Dict, List

from .v1_toleration import V1TolerationDict

V1alpha1SchedulingDict = TypedDict(
    "V1alpha1SchedulingDict",
    {
        "nodeSelector": Dict[str, str],
        "tolerations": List[V1TolerationDict],
    },
    total=False,
)
