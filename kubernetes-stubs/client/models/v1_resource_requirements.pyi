# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ResourceRequirements:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, limits: Any | None = ..., requests: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def limits(self): ...
    @limits.setter
    def limits(self, limits) -> None: ...
    @property
    def requests(self): ...
    @requests.setter
    def requests(self, requests) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
