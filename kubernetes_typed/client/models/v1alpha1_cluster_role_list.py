# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1ClusterRoleListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1alpha1_cluster_role import V1alpha1ClusterRoleDict

V1alpha1ClusterRoleListDict = TypedDict(
    "V1alpha1ClusterRoleListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1ClusterRoleDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
