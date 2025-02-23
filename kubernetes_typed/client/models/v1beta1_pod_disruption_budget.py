# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PodDisruptionBudgetDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1beta1_pod_disruption_budget_spec import V1beta1PodDisruptionBudgetSpecDict
from .v1beta1_pod_disruption_budget_status import V1beta1PodDisruptionBudgetStatusDict

V1beta1PodDisruptionBudgetDict = TypedDict(
    "V1beta1PodDisruptionBudgetDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1PodDisruptionBudgetSpecDict,
        "status": V1beta1PodDisruptionBudgetStatusDict,
    },
    total=False,
)
