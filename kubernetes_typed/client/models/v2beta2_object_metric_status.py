# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2ObjectMetricStatusDict generated type."""
from typing import TypedDict

from .v2beta2_cross_version_object_reference import V2beta2CrossVersionObjectReferenceDict
from .v2beta2_metric_identifier import V2beta2MetricIdentifierDict
from .v2beta2_metric_value_status import V2beta2MetricValueStatusDict

V2beta2ObjectMetricStatusDict = TypedDict(
    "V2beta2ObjectMetricStatusDict",
    {
        "current": V2beta2MetricValueStatusDict,
        "describedObject": V2beta2CrossVersionObjectReferenceDict,
        "metric": V2beta2MetricIdentifierDict,
    },
    total=False,
)
