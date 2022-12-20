from ..ass_tag_position import (AssTagMove, AssTagPosition)
from dataclasses import dataclass
from typing import Optional

@dataclass
class AssValidTagMove(AssTagMove):
    x1: float
    y1: float
    x2: float
    y2: float
    time1: Optional[float] = None
    time2: Optional[float] = None

    def __str__(self):
        if self.time1 is not None and self.time2 is not None:
            return f"\\{self.tag}({self.x1},{self.y1},{self.x2},{self.y2},{self.time1},{self.time2})"
        return f"\\{self.tag}({self.x1},{self.y1},{self.x2},{self.y2})"



@dataclass
class AssValidTagPosition(AssTagPosition):
    x: float
    y: float

    def __str__(self):
        return f"\\{self.tag}({self.x},{self.y})"

