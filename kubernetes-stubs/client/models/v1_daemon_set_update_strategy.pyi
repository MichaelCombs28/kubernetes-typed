# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1DaemonSetUpdateStrategy:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, rolling_update: Any | None = ..., type: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def rolling_update(self): ...
    @rolling_update.setter
    def rolling_update(self, rolling_update) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
