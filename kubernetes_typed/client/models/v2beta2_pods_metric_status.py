# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2PodsMetricStatusDict generated type."""
from typing import TypedDict

from .v2beta2_metric_identifier import V2beta2MetricIdentifierDict
from .v2beta2_metric_value_status import V2beta2MetricValueStatusDict

V2beta2PodsMetricStatusDict = TypedDict(
    "V2beta2PodsMetricStatusDict",
    {
        "current": V2beta2MetricValueStatusDict,
        "metric": V2beta2MetricIdentifierDict,
    },
    total=False,
)
