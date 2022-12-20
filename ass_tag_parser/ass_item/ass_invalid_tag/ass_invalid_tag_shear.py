from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_shear import (AssTagXShear, AssTagYShear)
from dataclasses import dataclass

@dataclass
class AssInvalidTagXShear(AssTagXShear, AssInvalidTag):
    pass

@dataclass
class AssInvalidTagYShear(AssTagYShear, AssInvalidTag):
    pass