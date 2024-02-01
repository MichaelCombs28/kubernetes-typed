# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1SubjectAccessReviewSpecDict generated type."""
from typing import TypedDict, Dict, List

from .v1_non_resource_attributes import V1NonResourceAttributesDict
from .v1_resource_attributes import V1ResourceAttributesDict

V1SubjectAccessReviewSpecDict = TypedDict(
    "V1SubjectAccessReviewSpecDict",
    {
        "extra": Dict[str, List[str]],
        "groups": List[str],
        "nonResourceAttributes": V1NonResourceAttributesDict,
        "resourceAttributes": V1ResourceAttributesDict,
        "uid": str,
        "user": str,
    },
    total=False,
)
