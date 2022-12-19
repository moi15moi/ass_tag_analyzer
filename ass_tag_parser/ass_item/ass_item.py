from abc import ABC, abstractmethod
from dataclasses import dataclass


class AssItem(ABC):
    @abstractmethod
    def __str__(self):
        return "{"


@dataclass
class AssTagListOpening(AssItem):
    def __str__(self):
        return "{"


@dataclass
class AssTagListEnding(AssItem):
    def __str__(self):
        return "}"


@dataclass
class AssText(AssItem):
    text: str

    def __str__(self):
        return self.text


@dataclass
class AssComment(AssItem):
    text: str

    def __str__(self):
        return self.text
