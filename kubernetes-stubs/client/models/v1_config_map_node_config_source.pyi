# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ConfigMapNodeConfigSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, kubelet_config_key: Any | None = ..., name: Any | None = ..., namespace: Any | None = ..., resource_version: Any | None = ..., uid: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def kubelet_config_key(self): ...
    @kubelet_config_key.setter
    def kubelet_config_key(self, kubelet_config_key) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def namespace(self): ...
    @namespace.setter
    def namespace(self, namespace) -> None: ...
    @property
    def resource_version(self): ...
    @resource_version.setter
    def resource_version(self, resource_version) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
