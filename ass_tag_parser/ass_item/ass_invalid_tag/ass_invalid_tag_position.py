from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_position import AssTagMove, AssTagPosition
from dataclasses import dataclass


@dataclass
class AssInvalidTagMove(AssTagMove, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagPosition(AssTagPosition, AssInvalidTag):
    pass
