from .ass_invalid_tag import AssInvalidTag
from ..ass_tag_karaoke import AssTagKaraoke, AssTagKaraokeFill, AssTagKaraokeOutline
from dataclasses import dataclass


@dataclass
class AssInvalidTagKaraoke(AssTagKaraoke, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagKaraokeFill(AssTagKaraokeFill, AssInvalidTag):
    pass


@dataclass
class AssInvalidTagKaraokeOutline(AssTagKaraokeOutline, AssInvalidTag):
    pass
