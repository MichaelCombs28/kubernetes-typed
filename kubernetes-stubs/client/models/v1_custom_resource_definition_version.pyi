# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1CustomResourceDefinitionVersion:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, additional_printer_columns: Any | None = ..., name: Any | None = ..., schema: Any | None = ..., served: Any | None = ..., storage: Any | None = ..., subresources: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def additional_printer_columns(self): ...
    @additional_printer_columns.setter
    def additional_printer_columns(self, additional_printer_columns) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def schema(self): ...
    @schema.setter
    def schema(self, schema) -> None: ...
    @property
    def served(self): ...
    @served.setter
    def served(self, served) -> None: ...
    @property
    def storage(self): ...
    @storage.setter
    def storage(self, storage) -> None: ...
    @property
    def subresources(self): ...
    @subresources.setter
    def subresources(self, subresources) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
