# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1JobCondition:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, last_probe_time: Any | None = ..., last_transition_time: Any | None = ..., message: Any | None = ..., reason: Any | None = ..., status: Any | None = ..., type: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def last_probe_time(self): ...
    @last_probe_time.setter
    def last_probe_time(self, last_probe_time) -> None: ...
    @property
    def last_transition_time(self): ...
    @last_transition_time.setter
    def last_transition_time(self, last_transition_time) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
