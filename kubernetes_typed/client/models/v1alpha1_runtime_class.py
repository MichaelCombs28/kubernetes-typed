# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1RuntimeClassDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1alpha1_runtime_class_spec import V1alpha1RuntimeClassSpecDict

V1alpha1RuntimeClassDict = TypedDict(
    "V1alpha1RuntimeClassDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1alpha1RuntimeClassSpecDict,
    },
    total=False,
)
