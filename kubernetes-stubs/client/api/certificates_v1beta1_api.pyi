# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any

class CertificatesV1beta1Api:
    api_client: Any
    def __init__(self, api_client: Any | None = ...) -> None: ...
    def create_certificate_signing_request(self, body, **kwargs): ...
    def create_certificate_signing_request_with_http_info(self, body, **kwargs): ...
    def delete_certificate_signing_request(self, name, **kwargs): ...
    def delete_certificate_signing_request_with_http_info(self, name, **kwargs): ...
    def delete_collection_certificate_signing_request(self, **kwargs): ...
    def delete_collection_certificate_signing_request_with_http_info(self, **kwargs): ...
    def get_api_resources(self, **kwargs): ...
    def get_api_resources_with_http_info(self, **kwargs): ...
    def list_certificate_signing_request(self, **kwargs): ...
    def list_certificate_signing_request_with_http_info(self, **kwargs): ...
    def patch_certificate_signing_request(self, name, body, **kwargs): ...
    def patch_certificate_signing_request_with_http_info(self, name, body, **kwargs): ...
    def patch_certificate_signing_request_status(self, name, body, **kwargs): ...
    def patch_certificate_signing_request_status_with_http_info(self, name, body, **kwargs): ...
    def read_certificate_signing_request(self, name, **kwargs): ...
    def read_certificate_signing_request_with_http_info(self, name, **kwargs): ...
    def read_certificate_signing_request_status(self, name, **kwargs): ...
    def read_certificate_signing_request_status_with_http_info(self, name, **kwargs): ...
    def replace_certificate_signing_request(self, name, body, **kwargs): ...
    def replace_certificate_signing_request_with_http_info(self, name, body, **kwargs): ...
    def replace_certificate_signing_request_approval(self, name, body, **kwargs): ...
    def replace_certificate_signing_request_approval_with_http_info(self, name, body, **kwargs): ...
    def replace_certificate_signing_request_status(self, name, body, **kwargs): ...
    def replace_certificate_signing_request_status_with_http_info(self, name, body, **kwargs): ...
