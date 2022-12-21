from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_font_scale import AssTagFontScale, AssTagFontXScale, AssTagFontYScale
from dataclasses import dataclass


@dataclass
class AssInvalidTagFontScale(AssTagFontScale, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagFontXScale(AssTagFontXScale, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagFontYScale(AssTagFontYScale, AssInvalidTag):
    pass
