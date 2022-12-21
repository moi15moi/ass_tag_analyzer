from ..ass_item import AssTag
from dataclasses import dataclass


@dataclass
class AssInvalidTag(AssTag):
    text: str

    def __str__(self):
        return f"\\{self.tag}{self.text}"
