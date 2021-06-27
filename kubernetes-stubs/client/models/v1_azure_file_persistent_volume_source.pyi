# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1AzureFilePersistentVolumeSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, read_only: Any | None = ..., secret_name: Any | None = ..., secret_namespace: Any | None = ..., share_name: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def secret_name(self): ...
    @secret_name.setter
    def secret_name(self, secret_name) -> None: ...
    @property
    def secret_namespace(self): ...
    @secret_namespace.setter
    def secret_namespace(self, secret_namespace) -> None: ...
    @property
    def share_name(self): ...
    @share_name.setter
    def share_name(self, share_name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
