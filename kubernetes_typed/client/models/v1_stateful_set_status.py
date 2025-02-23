# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1StatefulSetStatusDict generated type."""
from typing import TypedDict, List

from .v1_stateful_set_condition import V1StatefulSetConditionDict

V1StatefulSetStatusDict = TypedDict(
    "V1StatefulSetStatusDict",
    {
        "collisionCount": int,
        "conditions": List[V1StatefulSetConditionDict],
        "currentReplicas": int,
        "currentRevision": str,
        "observedGeneration": int,
        "readyReplicas": int,
        "replicas": int,
        "updateRevision": str,
        "updatedReplicas": int,
    },
    total=False,
)
