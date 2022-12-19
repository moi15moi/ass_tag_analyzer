from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag


@dataclass
class AssTagXRotation(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L487-L494
    angle: float

    def __str__(self):
        return f"\\{self.tag}{self.angle}"

    @property
    def tag(self) -> str:
        return "frx"


@dataclass
class AssTagYRotation(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L495-L502
    angle: float

    def __str__(self):
        return f"\\{self.tag}{self.angle}"

    @property
    def tag(self) -> str:
        return "fry"


@dataclass
class AssTagZRotation(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L503-L511
    angle: float
    is_short_tag: bool = False

    def __str__(self):
        if self.is_short_tag:
                return f"\\{self.short_tag}{self.angle}"
        return f"\\{self.tag}{self.angle}"

    @property
    def tag(self) -> str:
        return "frz"

    @property
    def short_tag(self) -> str:
        return "fr"
