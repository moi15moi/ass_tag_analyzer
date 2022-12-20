from ..ass_tag_rotation import (AssTagXRotation, AssTagYRotation, AssTagZRotation)
from dataclasses import dataclass


@dataclass
class AssValidTagXRotation(AssTagXRotation):
    angle: float

    def __str__(self):
        return f"\\{self.tag}{self.angle}"


@dataclass
class AssValidTagYRotation(AssTagYRotation):
    angle: float

    def __str__(self):
        return f"\\{self.tag}{self.angle}"


@dataclass
class AssValidTagZRotation(AssTagZRotation):
    angle: float

    def __str__(self):
        if self.is_short_tag:
                return f"\\{self.short_tag}{self.angle}"
        return f"\\{self.tag}{self.angle}"
