# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1RuntimeClassListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1alpha1_runtime_class import V1alpha1RuntimeClassDict

V1alpha1RuntimeClassListDict = TypedDict(
    "V1alpha1RuntimeClassListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1RuntimeClassDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
