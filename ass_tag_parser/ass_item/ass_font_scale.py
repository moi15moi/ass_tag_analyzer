from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag

@dataclass
class AssTagFontScale(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L410-L412

    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fsc"


@dataclass
class AssTagFontXScale(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L392-L400
    scale: float

    def __str__(self):
        return f"\\{self.tag}{self.scale}"

    @property
    def tag(self) -> str:
        return "fscx"


@dataclass
class AssTagFontYScale(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L401-L409
    scale: float

    def __str__(self):
        return f"\\{self.tag}{self.scale}"

    @property
    def tag(self) -> str:
        return "fscy"