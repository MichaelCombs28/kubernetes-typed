# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V2beta2ObjectMetricSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, described_object: Any | None = ..., metric: Any | None = ..., target: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def described_object(self): ...
    @described_object.setter
    def described_object(self, described_object) -> None: ...
    @property
    def metric(self): ...
    @metric.setter
    def metric(self, metric) -> None: ...
    @property
    def target(self): ...
    @target.setter
    def target(self, target) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
