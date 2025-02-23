# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1HorizontalPodAutoscalerDict generated type."""
from typing import TypedDict

from .v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpecDict
from .v1_horizontal_pod_autoscaler_status import V1HorizontalPodAutoscalerStatusDict
from .v1_object_meta import V1ObjectMetaDict

V1HorizontalPodAutoscalerDict = TypedDict(
    "V1HorizontalPodAutoscalerDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1HorizontalPodAutoscalerSpecDict,
        "status": V1HorizontalPodAutoscalerStatusDict,
    },
    total=False,
)
