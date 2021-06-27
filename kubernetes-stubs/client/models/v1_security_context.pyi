# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1SecurityContext:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, allow_privilege_escalation: Any | None = ..., capabilities: Any | None = ..., privileged: Any | None = ..., proc_mount: Any | None = ..., read_only_root_filesystem: Any | None = ..., run_as_group: Any | None = ..., run_as_non_root: Any | None = ..., run_as_user: Any | None = ..., se_linux_options: Any | None = ..., windows_options: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def allow_privilege_escalation(self): ...
    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation) -> None: ...
    @property
    def capabilities(self): ...
    @capabilities.setter
    def capabilities(self, capabilities) -> None: ...
    @property
    def privileged(self): ...
    @privileged.setter
    def privileged(self, privileged) -> None: ...
    @property
    def proc_mount(self): ...
    @proc_mount.setter
    def proc_mount(self, proc_mount) -> None: ...
    @property
    def read_only_root_filesystem(self): ...
    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem) -> None: ...
    @property
    def run_as_group(self): ...
    @run_as_group.setter
    def run_as_group(self, run_as_group) -> None: ...
    @property
    def run_as_non_root(self): ...
    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root) -> None: ...
    @property
    def run_as_user(self): ...
    @run_as_user.setter
    def run_as_user(self, run_as_user) -> None: ...
    @property
    def se_linux_options(self): ...
    @se_linux_options.setter
    def se_linux_options(self, se_linux_options) -> None: ...
    @property
    def windows_options(self): ...
    @windows_options.setter
    def windows_options(self, windows_options) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
