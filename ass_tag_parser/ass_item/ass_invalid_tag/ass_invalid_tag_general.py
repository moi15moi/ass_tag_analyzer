from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_general import (
    AssTagAnimation,
    AssTagBaselineOffset,
    AssTagBold,
    AssTagDraw,
    AssTagFontEncoding,
    AssTagFontName,
    AssTagFontSize,
    AssTagItalic,
    AssTagLetterSpacing,
    AssTagResetStyle,
    AssTagRotationOrigin,
    AssTagStrikeout,
    AssTagUnderline,
)
from dataclasses import dataclass


@dataclass
class AssInvalidTagAnimation(AssTagAnimation, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagBaselineOffset(AssTagBaselineOffset, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagBold(AssTagBold, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagDraw(AssTagDraw, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagFontEncoding(AssTagFontEncoding, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagFontName(AssTagFontName, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagFontSize(AssTagFontSize, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagItalic(AssTagItalic, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagLetterSpacing(AssTagLetterSpacing, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagResetStyle(AssTagResetStyle, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagRotationOrigin(AssTagRotationOrigin, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagStrikeout(AssTagStrikeout, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagUnderline(AssTagUnderline, AssInvalidTag):
    pass
