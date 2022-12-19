from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag



@dataclass
class AssTagColorAbstract(AssTag):
    red: int
    green: int
    blue: int

    def __str__(self):
        return f"\\{self.tag}&H{self.blue:02X}{self.green:02X}{self.red:02X}&"


@dataclass
class AssTagPrimaryColor(AssTagColorAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L705-L711
    short: bool = False

    @property
    def tag(self) -> str:
        return "1c"

    @property
    def short_tag(self) -> str:
        return "c"


@dataclass
class AssTagSecondaryColor(AssTagColorAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L712-L718

    @property
    def tag(self) -> str:
        return "2c"


@dataclass
class AssTagOutlineColor(AssTagColorAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L719-L725

    @property
    def tag(self) -> str:
        return "3c"


@dataclass
class AssTagBackgroundColor(AssTagColorAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L726-L732

    @property
    def tag(self) -> str:
        return "4c"
