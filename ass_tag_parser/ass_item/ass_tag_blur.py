from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag

@dataclass
class AssTagBlurEdges(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L768-L780
    weight: int

    def __str__(self):
        return f"\\{self.tag}{self.weight}"

    @property
    def tag(self) -> str:
        return "be"


@dataclass
class AssTagBlurEdgesGauss(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L381-L391
    __weight: float

    def __init__(self, weight: float):
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        self.__weight = 0 if value < 0 else value

    def __str__(self):
        return f"\\{self.tag}{self.weight}"

    @property
    def tag(self) -> str:
        return "blur"
