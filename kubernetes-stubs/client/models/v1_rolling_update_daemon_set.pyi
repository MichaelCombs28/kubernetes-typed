# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1RollingUpdateDaemonSet:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, max_unavailable: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def max_unavailable(self): ...
    @max_unavailable.setter
    def max_unavailable(self, max_unavailable) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
