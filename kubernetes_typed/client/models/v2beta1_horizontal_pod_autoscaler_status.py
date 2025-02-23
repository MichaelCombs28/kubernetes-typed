# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta1HorizontalPodAutoscalerStatusDict generated type."""
import datetime
from typing import TypedDict, List

from .v2beta1_horizontal_pod_autoscaler_condition import V2beta1HorizontalPodAutoscalerConditionDict
from .v2beta1_metric_status import V2beta1MetricStatusDict

V2beta1HorizontalPodAutoscalerStatusDict = TypedDict(
    "V2beta1HorizontalPodAutoscalerStatusDict",
    {
        "conditions": List[V2beta1HorizontalPodAutoscalerConditionDict],
        "currentMetrics": List[V2beta1MetricStatusDict],
        "currentReplicas": int,
        "desiredReplicas": int,
        "lastScaleTime": datetime.datetime,
        "observedGeneration": int,
    },
    total=False,
)
