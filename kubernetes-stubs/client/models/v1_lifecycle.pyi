# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1Lifecycle:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, post_start: Any | None = ..., pre_stop: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def post_start(self): ...
    @post_start.setter
    def post_start(self, post_start) -> None: ...
    @property
    def pre_stop(self): ...
    @pre_stop.setter
    def pre_stop(self, pre_stop) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
