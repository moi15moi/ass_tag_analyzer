from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag


@dataclass
class AssTagShadowAbstract(AssTag):
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
class AssTagShadow(AssTagShadowAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L817-L829

    @property
    def tag(self) -> str:
        return "shad"


@dataclass
class AssTagXShadow(AssTagShadowAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L329-L336

    @property
    def tag(self) -> str:
        return "xshad"


@dataclass
class AssTagYShadow(AssTagShadowAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L337-L344
    
    @property
    def tag(self) -> str:
        return "yshad"
