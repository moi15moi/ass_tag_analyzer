from ..ass_tag_shear import (AssTagXShear, AssTagYShear)
from dataclasses import dataclass

@dataclass
class AssValidTagXShear(AssTagXShear):
    value: float

    def __str__(self):
        return f"\\{self.tag}{self.value}"


@dataclass
class AssValidTagYShear(AssTagYShear):
    value: float

    def __str__(self):
        return f"\\{self.tag}{self.value}"