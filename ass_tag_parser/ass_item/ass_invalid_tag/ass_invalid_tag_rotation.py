from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_rotation import AssTagXRotation, AssTagYRotation, AssTagZRotation
from dataclasses import dataclass


@dataclass
class AssInvalidTagXRotation(AssTagXRotation, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagYRotation(AssTagYRotation, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagZRotation(AssTagZRotation, AssInvalidTag):
    pass
