# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1SelfSubjectAccessReviewSpecDict generated type."""
from typing import TypedDict

from .v1_non_resource_attributes import V1NonResourceAttributesDict
from .v1_resource_attributes import V1ResourceAttributesDict

V1SelfSubjectAccessReviewSpecDict = TypedDict(
    "V1SelfSubjectAccessReviewSpecDict",
    {
        "nonResourceAttributes": V1NonResourceAttributesDict,
        "resourceAttributes": V1ResourceAttributesDict,
    },
    total=False,
)
