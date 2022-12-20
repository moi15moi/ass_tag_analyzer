from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_alpha import (AssTagAlpha, AssTagPrimaryAlpha, AssTagSecondaryAlpha, AssTagOutlineAlpha, AssTagBackgroundAlpha)
from dataclasses import dataclass



@dataclass
class AssInvalidTagAlpha(AssTagAlpha, AssInvalidTag):
    pass


@dataclass
class AssInvalidPrimaryAlpha(AssTagPrimaryAlpha, AssInvalidTag):
    pass


@dataclass
class AssInvalidSecondaryAlpha(AssTagSecondaryAlpha, AssInvalidTag):
    pass


@dataclass
class AssInvalidOutlineAlpha(AssTagOutlineAlpha, AssInvalidTag):
    pass

@dataclass
class AssInvalidBackgroundAlpha(AssTagBackgroundAlpha, AssInvalidTag):
    pass
