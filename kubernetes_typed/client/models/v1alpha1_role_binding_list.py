# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1RoleBindingListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1alpha1_role_binding import V1alpha1RoleBindingDict

V1alpha1RoleBindingListDict = TypedDict(
    "V1alpha1RoleBindingListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1RoleBindingDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
