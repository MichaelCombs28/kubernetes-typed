# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1SessionAffinityConfig:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, client_ip: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def client_ip(self): ...
    @client_ip.setter
    def client_ip(self, client_ip) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
