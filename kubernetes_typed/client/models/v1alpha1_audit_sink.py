# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1AuditSinkDict generated type."""
from typing import TypedDict

from .v1_object_meta import V1ObjectMetaDict
from .v1alpha1_audit_sink_spec import V1alpha1AuditSinkSpecDict

V1alpha1AuditSinkDict = TypedDict(
    "V1alpha1AuditSinkDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1alpha1AuditSinkSpecDict,
    },
    total=False,
)
