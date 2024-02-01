# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1DeploymentDict generated type."""
from typing import TypedDict

from .v1_deployment_spec import V1DeploymentSpecDict
from .v1_deployment_status import V1DeploymentStatusDict
from .v1_object_meta import V1ObjectMetaDict

V1DeploymentDict = TypedDict(
    "V1DeploymentDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1DeploymentSpecDict,
        "status": V1DeploymentStatusDict,
    },
    total=False,
)
