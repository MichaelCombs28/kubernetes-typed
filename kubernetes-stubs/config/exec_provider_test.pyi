# Code generated by `stubgen`. DO NOT EDIT.
import unittest
from .config_exception import ConfigException as ConfigException
from .exec_provider import ExecProvider as ExecProvider
from .kube_config import ConfigNode as ConfigNode
from typing import Any

class ExecProviderTest(unittest.TestCase):
    input_ok: Any
    output_ok: str
    def setUp(self) -> None: ...
    def test_missing_input_keys(self) -> None: ...
    def test_error_code_returned(self, mock) -> None: ...
    def test_nonjson_output_returned(self, mock) -> None: ...
    def test_missing_output_keys(self, mock) -> None: ...
    def test_mismatched_api_version(self, mock) -> None: ...
    def test_ok_01(self, mock) -> None: ...
