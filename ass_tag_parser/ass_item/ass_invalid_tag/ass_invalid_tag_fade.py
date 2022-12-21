from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_fade import AssTagFade, AssTagFadeComplex
from dataclasses import dataclass


@dataclass
class AssInvalidTagFade(AssTagFade, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagFadeComplex(AssTagFadeComplex, AssInvalidTag):
    pass
