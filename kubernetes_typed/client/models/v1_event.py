# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1EventDict generated type."""
import datetime
from typing import TypedDict

from .v1_event_series import V1EventSeriesDict
from .v1_event_source import V1EventSourceDict
from .v1_object_meta import V1ObjectMetaDict
from .v1_object_reference import V1ObjectReferenceDict

V1EventDict = TypedDict(
    "V1EventDict",
    {
        "action": str,
        "apiVersion": str,
        "count": int,
        "eventTime": datetime.datetime,
        "firstTimestamp": datetime.datetime,
        "involvedObject": V1ObjectReferenceDict,
        "kind": str,
        "lastTimestamp": datetime.datetime,
        "message": str,
        "metadata": V1ObjectMetaDict,
        "reason": str,
        "related": V1ObjectReferenceDict,
        "reportingComponent": str,
        "reportingInstance": str,
        "series": V1EventSeriesDict,
        "source": V1EventSourceDict,
        "type": str,
    },
    total=False,
)
