from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag

@dataclass
class AssTagAlphaAbstract(AssTag):
    value: int

    def __str__(self):
        return f"\\{self.tag}&H{self.value}&"


@dataclass
class AssTagAlphaAbstract(AssTagAlphaAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L523-L539

    @property
    def tag(self) -> str:
        return "alpha"


@dataclass
class AssTagPrimaryAlpha(AssTagAlphaAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L733-L739

    @property
    def tag(self) -> str:
        return "1a"


@dataclass
class AssTagSecondaryAlpha(AssTagAlphaAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L740-L746

    @property
    def tag(self) -> str:
        return "2a"


@dataclass
class AssTagOutlineAlpha(AssTagAlphaAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L747-L753

    @property
    def tag(self) -> str:
        return "3a"


@dataclass
class AssTagBackgroundAlpha(AssTagAlphaAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L754-L760

    @property
    def tag(self) -> str:
        return "4a"
