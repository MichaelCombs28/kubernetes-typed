# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V2beta2HPAScalingRules:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, policies: Any | None = ..., select_policy: Any | None = ..., stabilization_window_seconds: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def policies(self): ...
    @policies.setter
    def policies(self, policies) -> None: ...
    @property
    def select_policy(self): ...
    @select_policy.setter
    def select_policy(self, select_policy) -> None: ...
    @property
    def stabilization_window_seconds(self): ...
    @stabilization_window_seconds.setter
    def stabilization_window_seconds(self, stabilization_window_seconds) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
