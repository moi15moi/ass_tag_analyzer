from dataclasses import dataclass
from ass_tag_parser.ass_item.ass_tag import AssTag

@dataclass
class AssTagXShear(AssTag):
    value: float

    def __str__(self):
        return f"\\{self.tag}{self.value}"

    @property
    def tag(self) -> str:
        return "fax"


@dataclass
class AssTagYShear(AssTag):
    value: float

    def __str__(self):
        return f"\\{self.tag}{self.value}"

    @property
    def tag(self) -> str:
        return "fay"