# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1EphemeralContainer:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, args: Any | None = ..., command: Any | None = ..., env: Any | None = ..., env_from: Any | None = ..., image: Any | None = ..., image_pull_policy: Any | None = ..., lifecycle: Any | None = ..., liveness_probe: Any | None = ..., name: Any | None = ..., ports: Any | None = ..., readiness_probe: Any | None = ..., resources: Any | None = ..., security_context: Any | None = ..., startup_probe: Any | None = ..., stdin: Any | None = ..., stdin_once: Any | None = ..., target_container_name: Any | None = ..., termination_message_path: Any | None = ..., termination_message_policy: Any | None = ..., tty: Any | None = ..., volume_devices: Any | None = ..., volume_mounts: Any | None = ..., working_dir: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def args(self): ...
    @args.setter
    def args(self, args) -> None: ...
    @property
    def command(self): ...
    @command.setter
    def command(self, command) -> None: ...
    @property
    def env(self): ...
    @env.setter
    def env(self, env) -> None: ...
    @property
    def env_from(self): ...
    @env_from.setter
    def env_from(self, env_from) -> None: ...
    @property
    def image(self): ...
    @image.setter
    def image(self, image) -> None: ...
    @property
    def image_pull_policy(self): ...
    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy) -> None: ...
    @property
    def lifecycle(self): ...
    @lifecycle.setter
    def lifecycle(self, lifecycle) -> None: ...
    @property
    def liveness_probe(self): ...
    @liveness_probe.setter
    def liveness_probe(self, liveness_probe) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def ports(self): ...
    @ports.setter
    def ports(self, ports) -> None: ...
    @property
    def readiness_probe(self): ...
    @readiness_probe.setter
    def readiness_probe(self, readiness_probe) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources) -> None: ...
    @property
    def security_context(self): ...
    @security_context.setter
    def security_context(self, security_context) -> None: ...
    @property
    def startup_probe(self): ...
    @startup_probe.setter
    def startup_probe(self, startup_probe) -> None: ...
    @property
    def stdin(self): ...
    @stdin.setter
    def stdin(self, stdin) -> None: ...
    @property
    def stdin_once(self): ...
    @stdin_once.setter
    def stdin_once(self, stdin_once) -> None: ...
    @property
    def target_container_name(self): ...
    @target_container_name.setter
    def target_container_name(self, target_container_name) -> None: ...
    @property
    def termination_message_path(self): ...
    @termination_message_path.setter
    def termination_message_path(self, termination_message_path) -> None: ...
    @property
    def termination_message_policy(self): ...
    @termination_message_policy.setter
    def termination_message_policy(self, termination_message_policy) -> None: ...
    @property
    def tty(self): ...
    @tty.setter
    def tty(self, tty) -> None: ...
    @property
    def volume_devices(self): ...
    @volume_devices.setter
    def volume_devices(self, volume_devices) -> None: ...
    @property
    def volume_mounts(self): ...
    @volume_mounts.setter
    def volume_mounts(self, volume_mounts) -> None: ...
    @property
    def working_dir(self): ...
    @working_dir.setter
    def working_dir(self, working_dir) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
