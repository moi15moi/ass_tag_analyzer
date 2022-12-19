from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag


@dataclass
class AssTagKaraokeAbstract(AssTag):
    duration: int  # In ms

    def __str__(self):
        return f"\\{self.tag}{self.duration // 10}"


@dataclass
class AssTagKaraoke(AssTagKaraokeAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L809-L816

    @property
    def tag(self) -> str:
        return "k"


@dataclass
class AssTagKaraokeFill(AssTagKaraokeAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L793-L800
    short_tag: bool = False

    def __str__(self):
        if self.short_tag:
            return f"\\{self.short_tag}{self.duration // 10}"
        return f"\\{self.tag}{self.duration // 10}"

    @property
    def tag(self) -> str:
        return "kf"

    @property
    def short_tag(self) -> str:
        return "K"


@dataclass
class AssTagKaraokeOutline(AssTagKaraokeAbstract):
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_parse.c#L801-L808

    @property
    def tag(self) -> str:
        return "ko"
