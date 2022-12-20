from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_blur import (AssTagBlurEdges, AssTagBlurEdgesGauss)
from dataclasses import dataclass

@dataclass
class AssInvalidTagBlurEdges(AssTagBlurEdges, AssInvalidTag):
    pass

@dataclass
class AssInvalidTagBlurEdgesGauss(AssTagBlurEdgesGauss, AssInvalidTag):
    pass