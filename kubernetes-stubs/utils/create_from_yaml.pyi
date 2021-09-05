# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes import client as client
from typing import Any

UPPER_FOLLOWED_BY_LOWER_RE: Any
LOWER_OR_NUM_FOLLOWED_BY_UPPER_RE: Any

def create_from_yaml(k8s_client, yaml_file: Any | None = ..., yaml_objects: Any | None = ..., verbose: bool = ..., namespace: str = ..., **kwargs): ...
def create_from_dict(k8s_client, data, verbose: bool = ..., namespace: str = ..., **kwargs): ...
def create_from_yaml_single_item(k8s_client, yml_object, verbose: bool = ..., **kwargs): ...

class FailToCreateError(Exception):
    api_exceptions: Any
    def __init__(self, api_exceptions) -> None: ...
