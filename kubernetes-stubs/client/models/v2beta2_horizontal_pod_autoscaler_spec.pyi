# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V2beta2HorizontalPodAutoscalerSpec:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, max_replicas: Any | None = ..., metrics: Any | None = ..., min_replicas: Any | None = ..., scale_target_ref: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def max_replicas(self): ...
    @max_replicas.setter
    def max_replicas(self, max_replicas) -> None: ...
    @property
    def metrics(self): ...
    @metrics.setter
    def metrics(self, metrics) -> None: ...
    @property
    def min_replicas(self): ...
    @min_replicas.setter
    def min_replicas(self, min_replicas) -> None: ...
    @property
    def scale_target_ref(self): ...
    @scale_target_ref.setter
    def scale_target_ref(self, scale_target_ref) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
