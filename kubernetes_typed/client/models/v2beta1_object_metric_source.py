# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta1ObjectMetricSourceDict generated type."""
from typing import TypedDict

from .v1_label_selector import V1LabelSelectorDict
from .v2beta1_cross_version_object_reference import V2beta1CrossVersionObjectReferenceDict

V2beta1ObjectMetricSourceDict = TypedDict(
    "V2beta1ObjectMetricSourceDict",
    {
        "averageValue": str,
        "metricName": str,
        "selector": V1LabelSelectorDict,
        "target": V2beta1CrossVersionObjectReferenceDict,
        "targetValue": str,
    },
    total=False,
)
