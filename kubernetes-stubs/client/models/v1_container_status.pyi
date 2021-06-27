# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1ContainerStatus:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, container_id: Any | None = ..., image: Any | None = ..., image_id: Any | None = ..., last_state: Any | None = ..., name: Any | None = ..., ready: Any | None = ..., restart_count: Any | None = ..., started: Any | None = ..., state: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def container_id(self): ...
    @container_id.setter
    def container_id(self, container_id) -> None: ...
    @property
    def image(self): ...
    @image.setter
    def image(self, image) -> None: ...
    @property
    def image_id(self): ...
    @image_id.setter
    def image_id(self, image_id) -> None: ...
    @property
    def last_state(self): ...
    @last_state.setter
    def last_state(self, last_state) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def ready(self): ...
    @ready.setter
    def ready(self, ready) -> None: ...
    @property
    def restart_count(self): ...
    @restart_count.setter
    def restart_count(self, restart_count) -> None: ...
    @property
    def started(self): ...
    @started.setter
    def started(self, started) -> None: ...
    @property
    def state(self): ...
    @state.setter
    def state(self, state) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
