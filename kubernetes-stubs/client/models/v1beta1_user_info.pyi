# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1UserInfo:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, extra: Any | None = ..., groups: Any | None = ..., uid: Any | None = ..., username: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def extra(self): ...
    @extra.setter
    def extra(self, extra) -> None: ...
    @property
    def groups(self): ...
    @groups.setter
    def groups(self, groups) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid) -> None: ...
    @property
    def username(self): ...
    @username.setter
    def username(self, username) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
