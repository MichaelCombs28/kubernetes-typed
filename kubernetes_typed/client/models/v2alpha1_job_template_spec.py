# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2alpha1JobTemplateSpecDict generated type."""
from typing import TypedDict

from .v1_job_spec import V1JobSpecDict
from .v1_object_meta import V1ObjectMetaDict

V2alpha1JobTemplateSpecDict = TypedDict(
    "V2alpha1JobTemplateSpecDict",
    {
        "metadata": V1ObjectMetaDict,
        "spec": V1JobSpecDict,
    },
    total=False,
)
