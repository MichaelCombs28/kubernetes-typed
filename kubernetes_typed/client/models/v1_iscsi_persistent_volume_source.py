# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ISCSIPersistentVolumeSourceDict generated type."""
from typing import TypedDict, List

from .v1_secret_reference import V1SecretReferenceDict

V1ISCSIPersistentVolumeSourceDict = TypedDict(
    "V1ISCSIPersistentVolumeSourceDict",
    {
        "chapAuthDiscovery": bool,
        "chapAuthSession": bool,
        "fsType": str,
        "initiatorName": str,
        "iqn": str,
        "iscsiInterface": str,
        "lun": int,
        "portals": List[str],
        "readOnly": bool,
        "secretRef": V1SecretReferenceDict,
        "targetPortal": str,
    },
    total=False,
)
