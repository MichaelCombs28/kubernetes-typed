# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1PreferredSchedulingTerm:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, preference: Any | None = ..., weight: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def preference(self): ...
    @preference.setter
    def preference(self, preference) -> None: ...
    @property
    def weight(self): ...
    @weight.setter
    def weight(self, weight) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
