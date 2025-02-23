# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1VolumeProjectionDict generated type."""
from typing import TypedDict

from .v1_config_map_projection import V1ConfigMapProjectionDict
from .v1_downward_api_projection import V1DownwardAPIProjectionDict
from .v1_secret_projection import V1SecretProjectionDict
from .v1_service_account_token_projection import V1ServiceAccountTokenProjectionDict

V1VolumeProjectionDict = TypedDict(
    "V1VolumeProjectionDict",
    {
        "configMap": V1ConfigMapProjectionDict,
        "downwardAPI": V1DownwardAPIProjectionDict,
        "secret": V1SecretProjectionDict,
        "serviceAccountToken": V1ServiceAccountTokenProjectionDict,
    },
    total=False,
)
