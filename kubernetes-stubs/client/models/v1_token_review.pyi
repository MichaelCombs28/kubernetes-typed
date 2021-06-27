# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1TokenReview:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, api_version: Any | None = ..., kind: Any | None = ..., metadata: Any | None = ..., spec: Any | None = ..., status: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata) -> None: ...
    @property
    def spec(self): ...
    @spec.setter
    def spec(self, spec) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
