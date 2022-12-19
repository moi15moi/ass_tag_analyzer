from ass_tag_parser.ass_item import AssItem
from dataclasses import dataclass


@dataclass
class AssInvalidTag(AssItem):
    @property
    def tag(self) -> str:
        pass


@dataclass
class AssInvalidTagBold(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "b"


@dataclass
class AssInvalidTagItalic(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "i"


@dataclass
class AssInvalidTagUnderline(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "u"


@dataclass
class AssInvalidTagStrikeout(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "s"


@dataclass
class AssInvalidTagBorder(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "bord"


@dataclass
class AssInvalidTagXBorder(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "xbord"


@dataclass
class AssInvalidTagYBorder(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "ybord"


@dataclass
class AssInvalidTagShadow(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "shad"


@dataclass
class AssInvalidTagXShadow(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "xshad"


@dataclass
class AssInvalidTagYShadow(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "yshad"


@dataclass
class AssInvalidTagBlurEdges(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "be"


@dataclass
class AssInvalidTagBlurEdgesGauss(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "blur"


@dataclass
class AssInvalidTagFontName:
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fn"


@dataclass
class AssInvalidTagFontEncoding(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fe"


@dataclass
class AssInvalidTagFontSize(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fs"


@dataclass
class AssInvalidTagFontScale(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fsc"


@dataclass
class AssInvalidTagFontXScale(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fscx"


@dataclass
class AssInvalidTagFontYScale(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fscy"


@dataclass
class AssInvalidTagLetterSpacing(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fsp"


@dataclass
class AssInvalidTagXRotation(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "frx"


@dataclass
class AssInvalidTagYRotation(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fry"


@dataclass
class AssInvalidTagZRotation(AssInvalidTag):
    short_tag: bool = False

    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "frz"

    @property
    def short_tag(self) -> str:
        return "fr"


@dataclass
class AssInvalidTagAlignment(AssInvalidTag):
    legacy: bool = False

    def __str__(self):
        if self.legacy:
            return f"\\{self.legacy_tag}"
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "an"

    @property
    def legacy_tag(self) -> str:
        return "a"


@dataclass
class AssInvalidTagResetStyle(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "r"


@dataclass
class AssInvalidTagKaraoke(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"


@dataclass
class AssInvalidTagKaraoke(AssInvalidTagKaraoke):
    @property
    def tag(self) -> str:
        return "k"


@dataclass
class AssInvalidTagKaraokeFill(AssInvalidTagKaraoke):
    short_tag: bool = False

    def __str__(self):
        if self.short_tag:
            return f"\\{self.short_tag}"
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "kf"

    @property
    def short_tag(self) -> str:
        return "K"


@dataclass
class AssInvalidTagKaraokeOutline(AssInvalidTagKaraoke):
    @property
    def tag(self) -> str:
        return "ko"


@dataclass
class AssInvalidTagColor(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"


@dataclass
class AssInvalidTagPrimaryColor(AssInvalidTagColor):
    short_tag: bool = False

    def __str__(self):
        if self.short_tag:
            return f"\\{self.short_tag}"
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "1c"

    @property
    def short_tag(self) -> str:
        return "c"


@dataclass
class AssInvalidTagSecondaryColor(AssInvalidTagColor):
    @property
    def tag(self) -> str:
        return "2c"


@dataclass
class AssInvalidTagOutlineColor(AssInvalidTagColor):
    @property
    def tag(self) -> str:
        return "3c"


@dataclass
class AssInvalidTagBackgroundColor(AssInvalidTagColor):
    @property
    def tag(self) -> str:
        return "4c"


@dataclass
class AssInvalidTagAlphaAbstract(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"


@dataclass
class AssInvalidTagAlpha(AssInvalidTagAlphaAbstract):
    @property
    def tag(self) -> str:
        return "alpha"


@dataclass
class AssInvalidTagPrimaryAlpha(AssInvalidTagAlphaAbstract):
    @property
    def tag(self) -> str:
        return "1a"


@dataclass
class AssInvalidTagSecondaryAlpha(AssInvalidTagAlphaAbstract):
    @property
    def tag(self) -> str:
        return "2a"


@dataclass
class AssInvalidTagOutlineAlpha(AssInvalidTagAlpha):
    @property
    def tag(self) -> str:
        return "3a"


@dataclass
class AssInvalidTagBackgroundAlpha(AssInvalidTagAlpha):
    @property
    def tag(self) -> str:
        return "4a"


@dataclass
class AssInvalidTagWrapStyle(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "q"


@dataclass
class AssInvalidTagFade(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fad"


@dataclass
class AssInvalidTagFadeComplex(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fade"


@dataclass
class AssInvalidTagXShear(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fax"


@dataclass
class AssInvalidTagYShear(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "fay"


@dataclass
class AssInvalidTagAnimation(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "t"


@dataclass
class AssInvalidTagBaselineOffset(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "pbo"


@dataclass
class AssInvalidTagDraw(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "p"


@dataclass
class AssInvalidTagMove(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "move"


@dataclass
class AssInvalidTagPosition(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "pos"


@dataclass
class AssInvalidTagRotationOrigin(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        return "org"


@dataclass
class AssInvalidTagClipRectangle(AssInvalidTag):
    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        if self.inverse:
            return "iclip"
        return "clip"


@dataclass
class AssInvalidTagClipVector(AssInvalidTag):
    inverse: bool = False

    def __str__(self):
        return f"\\{self.tag}"

    @property
    def tag(self) -> str:
        if self.inverse:
            return "iclip"
        return "clip"
