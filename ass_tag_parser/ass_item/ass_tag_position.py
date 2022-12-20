from .ass_item import AssTag
from dataclasses import dataclass

@dataclass
class AssTagMove(AssTag):

    @property
    def tag(self) -> str:
        return "move"


@dataclass
class AssTagPosition(AssTag):

    @property
    def tag(self) -> str:
        return "pos"
