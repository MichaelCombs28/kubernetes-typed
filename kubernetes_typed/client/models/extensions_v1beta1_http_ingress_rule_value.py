# Code generated by `typeddictgen`. DO NOT EDIT.
"""ExtensionsV1beta1HTTPIngressRuleValueDict generated type."""
from typing import TypedDict, List

from .extensions_v1beta1_http_ingress_path import ExtensionsV1beta1HTTPIngressPathDict

ExtensionsV1beta1HTTPIngressRuleValueDict = TypedDict(
    "ExtensionsV1beta1HTTPIngressRuleValueDict",
    {
        "paths": List[ExtensionsV1beta1HTTPIngressPathDict],
    },
    total=False,
)
