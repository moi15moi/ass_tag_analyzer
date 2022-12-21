from ass_tag_parser.ass_format import Format
from ..ass_tag_clip import AssTagClipRectangle, AssTagClipVector
from ...ass_draw.draw_struct import AssDrawCmd
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class AssValidTagClipRectangle(AssTagClipRectangle):
    x1: int
    y1: int
    x2: int
    y2: int

    def __str__(self):
        return f"\\{self.tag}({self.x1},{self.y1},{self.x2},{self.y2})"


@dataclass
class AssValidTagClipVector(AssTagClipVector):
    scale: Optional[int]
    path: List[AssDrawCmd]

    def __str__(self):
        raise Exception("Not implemented")
        # return f"\\{self.tag}({self.x1}, {self.y1}, {self.x2}, {self.y2})"
