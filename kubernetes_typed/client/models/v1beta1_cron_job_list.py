# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CronJobListDict generated type."""
from typing import TypedDict, List

from .v1_list_meta import V1ListMetaDict
from .v1beta1_cron_job import V1beta1CronJobDict

V1beta1CronJobListDict = TypedDict(
    "V1beta1CronJobListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1CronJobDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
