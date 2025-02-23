# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1JobDict generated type."""
from typing import TypedDict

from .v1_job_spec import V1JobSpecDict
from .v1_job_status import V1JobStatusDict
from .v1_object_meta import V1ObjectMetaDict

V1JobDict = TypedDict(
    "V1JobDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1JobSpecDict,
        "status": V1JobStatusDict,
    },
    total=False,
)
