# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1DeploymentSpecDict generated type."""
from typing import TypedDict

from .v1_deployment_strategy import V1DeploymentStrategyDict
from .v1_label_selector import V1LabelSelectorDict
from .v1_pod_template_spec import V1PodTemplateSpecDict

V1DeploymentSpecDict = TypedDict(
    "V1DeploymentSpecDict",
    {
        "minReadySeconds": int,
        "paused": bool,
        "progressDeadlineSeconds": int,
        "replicas": int,
        "revisionHistoryLimit": int,
        "selector": V1LabelSelectorDict,
        "strategy": V1DeploymentStrategyDict,
        "template": V1PodTemplateSpecDict,
    },
    total=False,
)
