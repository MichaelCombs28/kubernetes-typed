# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1CephFSVolumeSource:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, monitors: Any | None = ..., path: Any | None = ..., read_only: Any | None = ..., secret_file: Any | None = ..., secret_ref: Any | None = ..., user: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def monitors(self): ...
    @monitors.setter
    def monitors(self, monitors) -> None: ...
    @property
    def path(self): ...
    @path.setter
    def path(self, path) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only) -> None: ...
    @property
    def secret_file(self): ...
    @secret_file.setter
    def secret_file(self, secret_file) -> None: ...
    @property
    def secret_ref(self): ...
    @secret_ref.setter
    def secret_ref(self, secret_ref) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
