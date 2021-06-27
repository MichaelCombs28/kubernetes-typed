# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any

class SchedulingV1alpha1Api:
    api_client: Any
    def __init__(self, api_client: Any | None = ...) -> None: ...
    def create_priority_class(self, body, **kwargs): ...
    def create_priority_class_with_http_info(self, body, **kwargs): ...
    def delete_collection_priority_class(self, **kwargs): ...
    def delete_collection_priority_class_with_http_info(self, **kwargs): ...
    def delete_priority_class(self, name, **kwargs): ...
    def delete_priority_class_with_http_info(self, name, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_priority_class(self, **kwargs): ...
    def list_priority_class_with_http_info(self, **kwargs): ...
    def patch_priority_class(self, name, body, **kwargs): ...
    def patch_priority_class_with_http_info(self, name, body, **kwargs): ...
    def read_priority_class(self, name, **kwargs): ...
    def read_priority_class_with_http_info(self, name, **kwargs): ...
    def replace_priority_class(self, name, body, **kwargs): ...
    def replace_priority_class_with_http_info(self, name, body, **kwargs): ...
