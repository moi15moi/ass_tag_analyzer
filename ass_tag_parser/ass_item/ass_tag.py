from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from ass_item import AssItem


class AssTag(AssItem):
    @property
    @abstractmethod
    def tag(self) -> str:
        pass


@dataclass
class AssTagBold(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L781-L786
    __weight: int

    def __init__(self, weight: int):
        weight = 400 if weight == 0 else weight
        weight = 700 if weight == 1 else weight

        if weight < 100:
            raise ValueError("Bold cannot be under 100.")

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

    @property
    def tag(self) -> str:
        return "b"


@dataclass
class AssTagItalic(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L787-L792
    enabled: bool

    def __str__(self):
        return f"\\{self.tag}{int(self.enabled)}"

    @property
    def tag(self) -> str:
        return "i"


@dataclass
class AssTagUnderline(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L838-L845
    enabled: bool

    def __str__(self):
        return f"\\{self.tag}{int(self.enabled)}"

    @property
    def tag(self) -> str:
        return "u"


@dataclass
class AssTagStrikeout(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L830-L837
    enabled: bool

    def __str__(self):
        return f"\\{self.tag}{int(self.enabled)}"

    @property
    def tag(self) -> str:
        return "s"



@dataclass
class AssTagFontName:
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L512-L522

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"\\{self.tag}{self.name}"

    @property
    def tag(self) -> str:
        return "fn"


@dataclass
class AssTagFontEncoding(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L858-L864
    encoding: int

    def __str__(self):
        return f"\\{self.tag}{self.encoding}"

    @property
    def tag(self) -> str:
        return "fe"


@dataclass
class AssTagFontSize(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L421-L432
    size: float

    def __str__(self):
        return f"\\{self.tag}{self.size}"

    @property
    def tag(self) -> str:
        return "fs"



@dataclass
class AssTagLetterSpacing(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L413-L420
    spacing: float

    def __str__(self):
        return f"\\{self.tag}{self.spacing}"

    @property
    def tag(self) -> str:
        return "fsp"




@dataclass
class AssTagAlignment(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L540-L561
    alignment: int
    legacy: bool = False

    def __init__(self, alignment: int, legacy: bool = False):
        self.legacy = legacy

        if self.legacy:
            # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L553
            if 1 <= alignment <= 11:
                self.alignment = alignment
            else:
                raise ValueError(
                    "Legacy Alignment need to be between 1 and 11 inclusive"
                )
        else:
            # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L543
            if 1 <= alignment <= 9:
                self.alignment = alignment
            else:
                raise ValueError(
                    "Alignment need to be between 1 and 9 inclusive"
                )

    def __str__(self):
        if self.legacy:
            return f"\\{self.legacy_tag}{self.alignment}"
        return f"\\{self.tag}{self.alignment}"

    @property
    def tag(self) -> str:
        return "an"

    @property
    def legacy_tag(self) -> str:
        return "a"


@dataclass
class AssTagResetStyle(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L761-L767
    style: str

    def __str__(self):
        return f"\\{self.tag}{self.style}"

    @property
    def tag(self) -> str:
        return "r"


class WrapStyle(Enum):

    SMART_TOP = 0
    END_OF_LINE = 1
    NO_WORD = 2
    SMART_BOTTOM = 3


@dataclass
class AssTagWrapStyle(AssTag):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L853-L857
    style: WrapStyle

    def __str__(self):
        return f"\\{self.tag}{self.style.value}"

    @property
    def tag(self) -> str:
        return "q"


@dataclass
class AssTagAnimation(AssTag):
    tags: List[AssItem]
    acceleration: float = 1.0
    time1: Optional[int] = None
    time2: Optional[int] = None

    def __str__(self):
        if (
            self.time1 is not None
            and self.time2 is not None
            and self.acceleration is not None
        ):
            return f"\\{self.tag}({self.time1}, {self.time2}, {self.acceleration}, {self.tags})"
        elif self.time1 is not None and self.time2 is not None:
            return f"\\{self.tag}({self.time1}, {self.time2}, {self.tags})"
        else:
            return f"\\{self.tag}({self.tags})"

    @property
    def tag(self) -> str:
        return "t"


@dataclass
class AssTagBaselineOffset(AssTag):
    # https://github.com/libass/libass/blob/5f57443f1784434fe8961275da08be6d6febc688/libass/ass_parse.c#L846-L848
    offset: float

    def __str__(self):
        return f"\\{self.tag}{self.offset}"

    @property
    def tag(self) -> str:
        return "pbo"


@dataclass
class AssTagRotationOrigin(AssTag):
    x: float
    y: float

    def __str__(self):
        return f"\\{self.tag}({self.x}, {self.y})"

    @property
    def tag(self) -> str:
        return "org"


@dataclass
class AssTagDraw(AssTag):
    # https://github.com/libass/libass/blob/5f57443f1784434fe8961275da08be6d6febc688/libass/ass_parse.c#L849-L852
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

    @property
    def tag(self) -> str:
        return "p"

