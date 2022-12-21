from ass_tag_parser.ass_format import Format
from ..ass_tag_font_scale import AssTagFontScale, AssTagFontXScale, AssTagFontYScale
from dataclasses import dataclass


@dataclass
class AssValidTagFontScale(AssTagFontScale):
    def __str__(self):
        return f"\\{self.tag}"


@dataclass
class AssValidTagFontXScale(AssTagFontXScale):
    scale: float

    def __str__(self):
        return f"\\{self.tag}{Format.format_float(self.scale)}"


@dataclass
class AssValidTagFontYScale(AssTagFontYScale):
    scale: float

    def __str__(self):
        return f"\\{self.tag}{Format.format_float(self.scale)}"
