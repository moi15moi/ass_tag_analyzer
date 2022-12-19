from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag


@dataclass
class AssTagBorderAbstract(AssTag):
    __size: float

    def __init__(self, size: float):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: float):
        self.__size = 0 if value < 0 else value

    def __str__(self):
        return f"\\{self.tag}{self.size}"


@dataclass
class AssTagBorder(AssTagBorderAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L433-L444

    @property
    def tag(self) -> str:
        return "bord"


@dataclass
class AssTagXBorder(AssTagBorderAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L311-L319

    @property
    def tag(self) -> str:
        return "xbord"


@dataclass
class AssTagYBorder(AssTagBorderAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L320-L328

    @property
    def tag(self) -> str:
        return "ybord"