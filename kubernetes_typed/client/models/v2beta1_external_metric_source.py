# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta1ExternalMetricSourceDict generated type."""
from typing import TypedDict

from .v1_label_selector import V1LabelSelectorDict

V2beta1ExternalMetricSourceDict = TypedDict(
    "V2beta1ExternalMetricSourceDict",
    {
        "metricName": str,
        "metricSelector": V1LabelSelectorDict,
        "targetAverageValue": str,
        "targetValue": str,
    },
    total=False,
)
