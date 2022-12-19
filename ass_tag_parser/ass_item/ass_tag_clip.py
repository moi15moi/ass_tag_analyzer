from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag

@dataclass
class AssTagClipRectangle(AssTag):
    x1: float
    y1: float
    x2: float
    y2: float
    inverse: bool

    def __str__(self):
        return f"\\{self.tag}({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    @property
    def tag(self) -> str:
        if self.inverse:
            return "iclip"
        return "clip"


@dataclass
class AssTagClipVector(AssTag):
    scale: Optional[int]
    path: list[AssDrawCmd]
    inverse: bool

    def __str__(self):
        return f"\\{self.tag}({self.x1}, {self.y1}, {self.x2}, {self.y2})"

    @property
    def tag(self) -> str:
        if self.inverse:
            return "iclip"
        return "clip"
