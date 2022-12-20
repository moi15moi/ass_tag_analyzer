from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class AssDrawPoint:
    x: float
    y: float


class AssDrawCmd:
    pass


@dataclass
class AssDrawCmdMove(AssDrawCmd):
    pos: AssDrawPoint
    close: bool


@dataclass
class AssDrawCmdLine(AssDrawCmd):
    points: List[AssDrawPoint]


@dataclass
class AssDrawCmdBezier(AssDrawCmd):
    points: Tuple[AssDrawPoint, AssDrawPoint, AssDrawPoint]


@dataclass
class AssDrawCmdSpline(AssDrawCmd):
    points: List[AssDrawPoint]


@dataclass
class AssDrawCmdExtendSpline(AssDrawCmd):
    points: List[AssDrawPoint]


@dataclass
class AssDrawCmdCloseSpline(AssDrawCmd):
    pass
