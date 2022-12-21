from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_clip import AssTagClipRectangle, AssTagClipVector
from dataclasses import dataclass


@dataclass
class AssInvalidTagClipRectangle(AssTagClipRectangle, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagClipVector(AssTagClipVector, AssInvalidTag):
    pass
