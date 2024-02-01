# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2ObjectMetricSourceDict generated type."""
from typing import TypedDict

from .v2beta2_cross_version_object_reference import V2beta2CrossVersionObjectReferenceDict
from .v2beta2_metric_identifier import V2beta2MetricIdentifierDict
from .v2beta2_metric_target import V2beta2MetricTargetDict

V2beta2ObjectMetricSourceDict = TypedDict(
    "V2beta2ObjectMetricSourceDict",
    {
        "describedObject": V2beta2CrossVersionObjectReferenceDict,
        "metric": V2beta2MetricIdentifierDict,
        "target": V2beta2MetricTargetDict,
    },
    total=False,
)
