# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1TokenReviewStatusDict generated type."""
from typing import TypedDict, List

from .v1_user_info import V1UserInfoDict

V1TokenReviewStatusDict = TypedDict(
    "V1TokenReviewStatusDict",
    {
        "audiences": List[str],
        "authenticated": bool,
        "error": str,
        "user": V1UserInfoDict,
    },
    total=False,
)
