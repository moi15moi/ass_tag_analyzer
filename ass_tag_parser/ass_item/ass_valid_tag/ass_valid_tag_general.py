from ass_tag_parser.ass_item.ass_item import AssItem
from ..ass_tag_general import (
    AssTagAlignment,
    AssTagAnimation,
    AssTagBaselineOffset, 
    AssTagBold,
    AssTagDraw, AssTagFontEncoding, AssTagFontName, AssTagFontSize, AssTagItalic, AssTagLetterSpacing, AssTagResetStyle, AssTagRotationOrigin, AssTagStrikeout, AssTagUnderline
)
from dataclasses import dataclass
from typing import List, Optional


from ...ass_type_parser import strip_whitespace

@dataclass
class AssValidTagBold(AssTagBold):
    __weight: int

    def __init__(self, weight: float):
        self.weight = weight


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        weight = 400 if weight == 0 else weight
        weight = 700 if weight == 1 else weight

        self.__weight = weight

    def __str__(self):
        return f"\\{self.tag}{self.weight}"



@dataclass
class AssValidTagItalic(AssTagItalic):
    enabled: bool

    def __str__(self):
        return f"\\{self.tag}{int(self.enabled)}"


@dataclass
class AssValidTagUnderline(AssTagUnderline):
    enabled: bool

    def __str__(self):
        return f"\\{self.tag}{int(self.enabled)}"



@dataclass
class AssValidTagStrikeout(AssTagStrikeout):
    enabled: bool

    def __str__(self):
        return f"\\{self.tag}{int(self.enabled)}"




@dataclass
class AssValidTagFontName(AssTagFontName):
    __name: str

    def __init__(self, name: int):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = strip_whitespace(name)

    def __str__(self):
        return f"\\{self.tag}{self.name}"


@dataclass
class AssValidTagFontEncoding(AssTagFontEncoding):
    encoding: int

    def __str__(self):
        return f"\\{self.tag}{self.encoding}"



@dataclass
class AssValidTagFontSize(AssTagFontSize):
    size: float

    def __str__(self):
        return f"\\{self.tag}{self.size}"




@dataclass
class AssValidTagLetterSpacing(AssTagLetterSpacing):
    spacing: float

    def __str__(self):
        return f"\\{self.tag}{self.spacing}"





@dataclass
class AssValidTagAlignment(AssTagAlignment):
    __alignment: int

    def __init__(self, alignment: int, is_legacy_tag: bool = False):
        self.is_legacy_tag = is_legacy_tag
        self.alignment = alignment


    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: int):
        if self.is_legacy_tag:
            # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L553
            if 1 <= alignment <= 11:
                self.__alignment = alignment
            else:
                raise ValueError(
                    "Legacy Alignment need to be between 1 and 11 inclusive"
                )
        else:
            # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L543
            if 1 <= alignment <= 9:
                self.__alignment = alignment
            else:
                raise ValueError(
                    "Alignment need to be between 1 and 9 inclusive"
                )
    def __str__(self):
        if self.is_legacy_tag:
            return f"\\{self.legacy_tag}{self.alignment}"
        return f"\\{self.tag}{self.alignment}"


@dataclass
class AssValidTagResetStyle(AssTagResetStyle):
    style: str

    def __str__(self):
        return f"\\{self.tag}{self.style}"



@dataclass
class AssValidTagAnimation(AssTagAnimation):
    tags: List[AssItem]
    acceleration: float = 1.0
    time1: Optional[int] = None
    time2: Optional[int] = None

    def __str__(self):
        tags_text = ','.join([str(tag) for tag in self.tags])

        if (
            self.time1 is not None
            and self.time2 is not None
            and self.acceleration is not None and self.acceleration != 1
        ):
            return f"\\{self.tag}({self.time1},{self.time2},{self.acceleration},{tags_text})"
        elif self.time1 is not None and self.time2 is not None:
            return f"\\{self.tag}({self.time1},{self.time2},{tags_text})"
        else:
            return f"\\{self.tag}({tags_text})"

@dataclass
class AssValidTagBaselineOffset(AssTagBaselineOffset):
    offset: float

    def __str__(self):
        return f"\\{self.tag}{self.offset}"



@dataclass
class AssValidTagRotationOrigin(AssTagRotationOrigin):
    x: float
    y: float

    def __str__(self):
        return f"\\{self.tag}({self.x}, {self.y})"




@dataclass
class AssValidTagDraw(AssTagDraw):
    __scale: int

    def __init__(self, scale: int):
        self.scale = scale

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, value: int):
        self.__scale = 0 if value < 0 else value

    def __str__(self):
        return f"\\{self.tag}{self.scale}"
