# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V2beta1HorizontalPodAutoscalerStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, conditions: Any | None = ..., current_metrics: Any | None = ..., current_replicas: Any | None = ..., desired_replicas: Any | None = ..., last_scale_time: Any | None = ..., observed_generation: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions) -> None: ...
    @property
    def current_metrics(self): ...
    @current_metrics.setter
    def current_metrics(self, current_metrics) -> None: ...
    @property
    def current_replicas(self): ...
    @current_replicas.setter
    def current_replicas(self, current_replicas) -> None: ...
    @property
    def desired_replicas(self): ...
    @desired_replicas.setter
    def desired_replicas(self, desired_replicas) -> None: ...
    @property
    def last_scale_time(self): ...
    @last_scale_time.setter
    def last_scale_time(self, last_scale_time) -> None: ...
    @property
    def observed_generation(self): ...
    @observed_generation.setter
    def observed_generation(self, observed_generation) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
