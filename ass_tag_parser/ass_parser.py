# from collections import Counter
# import re
# from dataclasses import dataclass
# from functools import cache
# from typing import Any, Iterable, List, Optional, Union
# import string
# from itertools import takewhile

# from ass_tag_parser.ass_item.ass_valid_tag import (
#     AssTag,
#     AssTagAlignment,
#     AssTagAlpha,
#     AssTagBackgroundAlpha,
#     AssTagBackgroundColor,
#     AssTagBlurEdges,
#     AssTagBlurEdgesGauss,
#     AssTagBold,
#     AssTagBorder,
#     AssTagClipRectangle,
#     AssTagFade,
#     AssTagFadeComplex,
#     AssTagFontEncoding,
#     AssTagFontName,
#     AssTagOutlineAlpha,
#     AssTagOutlineColor,
#     AssTagPrimaryAlpha,
#     AssTagPrimaryColor,
#     AssTagSecondaryAlpha,
#     AssTagSecondaryColor,
#     AssTagXShear,
#     AssTagYShear,
# )

# from ass_tag_parser.ass_item.ass_invalid_tag.ass_invalid_tag import AssInvalidTagPrimaryColor
# from ass_tag_parser.ass_item.ass_invalid_tag.ass_invalid_tag import (
#     AssInvalidTagAlignment,
#     AssInvalidTagAlpha,
#     AssInvalidTagBackgroundAlpha,
#     AssInvalidTagBackgroundColor,
#     AssInvalidTagBaselineOffset,
#     AssInvalidTagBlurEdges,
#     AssInvalidTagBlurEdgesGauss,
#     AssInvalidTagBold,
#     AssInvalidTagBorder,
#     AssInvalidTagFontEncoding,
#     AssInvalidTagFontScale,
#     AssInvalidTagFontSize,
#     AssInvalidTagFontXScale,
#     AssInvalidTagFontYScale,
#     AssInvalidTagItalic,
#     AssInvalidTagLetterSpacing,
#     AssInvalidTagOutlineAlpha,
#     AssInvalidTagOutlineColor,
#     AssInvalidTagPrimaryAlpha,
#     AssInvalidTagSecondaryAlpha,
#     AssInvalidTagSecondaryColor,
#     AssInvalidTagShadow,
#     AssInvalidTagStrikeout,
#     AssInvalidTagUnderline,
#     AssInvalidTagXBorder,
#     AssInvalidTagXRotation,
#     AssInvalidTagXShadow,
#     AssInvalidTagXShear,
#     AssInvalidTagYBorder,
#     AssInvalidTagYRotation,
#     AssInvalidTagYShadow,
#     AssInvalidTagYShear,
#     AssInvalidTagZRotation,
# )
# from ass_tag_parser.ass_item.ass_item import (
#     AssItem,
#     AssTagListEnding,
#     AssTagListOpening,
#     AssText,
# )
# from ass_tag_parser.ass_item.ass_valid_tag import (
#     AssTagAnimation,
#     AssTagBaselineOffset,
#     AssTagDraw,
#     AssTagFontScale,
#     AssTagFontSize,
#     AssTagFontXScale,
#     AssTagFontYScale,
#     AssTagItalic,
#     AssTagKaraoke,
#     AssTagKaraokeFill,
#     AssTagKaraokeOutline,
#     AssTagLetterSpacing,
#     AssTagMove,
#     AssTagPosition,
#     AssTagResetStyle,
#     AssTagRotationOrigin,
#     AssTagShadow,
#     AssTagStrikeout,
#     AssTagUnderline,
#     AssTagWrapStyle,
#     AssTagXBorder,
#     AssTagXRotation,
#     AssTagXShadow,
#     AssTagYBorder,
#     AssTagYRotation,
#     AssTagYShadow,
#     AssTagZRotation,
#     WrapStyle,
# )


# from ass_tag_parser.ass_type_parser import (
#     color_arg,
#     float_str_to_float,
#     hex_str_to_int,
#     int_str_to_int,
#     int_to_int32,
# )
# from ass_tag_parser.draw_parser import parse_draw_commands
# from ass_tag_parser.errors import (
#     BadAssTagArgument,
#     ParseError,
#     UnexpectedCurlyBrace,
#     UnknownTag,
#     UnterminatedCurlyBrace,
# )
# from ass_tag_parser.io import MyIO

# def strip_whitespace(text: str) -> str:
#     """Remove whitespace from text.

#     Inpired by: https://github.com/libass/libass/blob/5f57443f1784434fe8961275da08be6d6febc688/libass/ass_utils.c#L160-L174

#     Parameters:
#         text (str): An string.
#     Returns:
#         A string without whitespace at the beginning and at the end.
#     """

#     return text.strip(" \t")


# def parse_tags(text: str, pwr: float, nested: bool) -> List[AssTag]:
#     # https://github.com/libass/libass/blob/5f57443f1784434fe8961275da08be6d6febc688/libass/ass_parse.c#L242-L869
#     # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l1383
#     tags: List[AssTag] = []
#     i = 0

#     while (j := text.find("\\", i)) >= 0:
#         # Skip the \
#         j += 1

#         cmd: str = ""
#         for c in text[j:]:
#             if c in ("(", "\\"):
#                 break
#             else:
#                 cmd += c
#                 j += 1

#         cmd = strip_whitespace(cmd)

#         if len(cmd) == 0:
#             i = j
#             continue

#         params: List[str] = []

#         if j < len(text) and text[j] == "(":

#             param: str = ""
#             # Skip the (
#             j += 1
#             for c in text[j:]:
#                 if c == ")":
#                     break
#                 else:
#                     param += c
#                     j += 1

#             param.strip(" \t")

#             temp_j = j

#             while len(param) != 0:
#                 i = param.find(",")
#                 j = param.find("\\")

#                 if i >= 0 and (j < 0 or i < j):
#                     s = param[:i].strip(" \t")
#                     if len(s) != 0:
#                         params.append(s)
#                     param = param[i + 1 :] if i + 1 < len(param) else ""
#                 else:
#                     param.strip(" \t")
#                     if len(param) != 0:
#                         params.append(param)
#                     param = ""

#             j = temp_j

#         if cmd.startswith(("1c", "2c", "3c", "4c")):
#             params.append(cmd[2:].strip("&H"))
#             cmd = cmd[:2]
#         elif cmd.startswith(("1a", "2a", "3a", "4a")):
#             params.append(cmd[2:].strip("&H"))
#             cmd = cmd[:2]
#         elif cmd.startswith("alpha"):
#             params.append(cmd[5:].strip("&H"))
#             cmd = cmd[:5]
#         elif cmd.startswith("an"):
#             params.append(cmd[2:])
#             cmd = cmd[:2]
#         elif cmd.startswith("a"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith("blur"):
#             params.append(cmd[4:])
#             cmd = cmd[:4]
#         elif cmd.startswith("bord"):
#             params.append(cmd[4:])
#             cmd = cmd[:4]
#         elif cmd.startswith("be"):
#             params.append(cmd[2:])
#             cmd = cmd[:2]
#         elif cmd.startswith("b"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith("clip"):
#             pass
#         elif cmd.startswith("c"):
#             params.append(cmd[1:].strip("&H"))
#             cmd = cmd[:1]
#         elif cmd.startswith("fade"):
#             pass
#         elif cmd.startswith("fe"):
#             params.append(cmd[2:])
#             cmd = cmd[:2]
#         elif cmd.startswith("fn"):
#             params.append(cmd[2:])
#             cmd = cmd[:2]
#         elif cmd.startswith(("frx", "fry", "frz")):
#             params.append(cmd[3:])
#             cmd = cmd[:3]
#         elif cmd.startswith(("fax", "fay")):
#             params.append(cmd[3:])
#             cmd = cmd[:3]
#         elif cmd.startswith("fr"):
#             params.append(cmd[2:])
#             cmd = cmd[:2]
#         elif cmd.startswith(("fscx", "fscy")):
#             params.append(cmd[4:])
#             cmd = cmd[:4]
#         elif cmd.startswith("fsc"):
#             params.append(cmd[3:])
#             cmd = cmd[:3]
#         elif cmd.startswith("fsp"):
#             params.append(cmd[3:])
#             cmd = cmd[:3]
#         elif cmd.startswith("fs"):
#             params.append(cmd[2:])
#             cmd = cmd[:2]
#         elif cmd.startswith("iclip"):
#             pass
#         elif cmd.startswith("i"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith(("kt", "kf", "ko")):
#             params.append(cmd[2:])
#             cmd = cmd[:2]
#         elif cmd.startswith(("k", "K")):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith("move"):
#             pass
#         elif cmd.startswith("org"):
#             pass
#         elif cmd.startswith("pbo"):
#             params.append(cmd[3:])
#             cmd = cmd[:3]
#         elif cmd.startswith("pos"):
#             pass
#         elif cmd.startswith("p"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith("q"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith("r"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith("shad"):
#             params.append(cmd[4:])
#             cmd = cmd[:4]
#         elif cmd.startswith("s"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith("t"):
#             pass
#         elif cmd.startswith("u"):
#             params.append(cmd[1:])
#             cmd = cmd[:1]
#         elif cmd.startswith(("xbord", "xshad", "ybord", "yshad")):
#             params.append(cmd[5:])
#             cmd = cmd[:5]

#         p = params[0] if len(params) > 0 else ""

#         if cmd in ("1c", "2c", "3c", "4c"):
#             i = ord(cmd[0]) - ord("0")

#             if len(p) == 0:
#                 if i == 1:
#                     tags.append(AssInvalidTagPrimaryColor())
#                 elif i == 2:
#                     tags.append(AssInvalidTagSecondaryColor())
#                 elif i == 3:
#                     tags.append(AssInvalidTagOutlineColor())
#                 elif i == 4:
#                     tags.append(AssInvalidTagBackgroundColor())

#             else:
#                 red, green, blue = color_arg(int_to_int32(hex_str_to_int(p)))

#                 if i == 1:
#                     tags.append(AssTagPrimaryColor(red, green, blue))
#                 elif i == 2:
#                     tags.append(AssTagSecondaryColor(red, green, blue))
#                 elif i == 3:
#                     tags.append(AssTagOutlineColor(red, green, blue))
#                 elif i == 4:
#                     tags.append(AssTagBackgroundColor(red, green, blue))

#         elif cmd in ("1a", "2a", "3a", "4a"):
#             i = ord(cmd[0]) - ord("0")

#             if len(p) == 0:
#                 if i == 1:
#                     tags.append(AssInvalidTagPrimaryAlpha())
#                 elif i == 2:
#                     tags.append(AssInvalidTagSecondaryAlpha())
#                 elif i == 3:
#                     tags.append(AssInvalidTagOutlineAlpha())
#                 elif i == 4:
#                     tags.append(AssInvalidTagBackgroundAlpha())
#             else:

#                 alpha_arg = int_to_int32(hex_str_to_int(p))

#                 if i == 1:
#                     tags.append(AssTagPrimaryAlpha(alpha_arg))
#                 elif i == 2:
#                     tags.append(AssTagSecondaryAlpha(alpha_arg))
#                 elif i == 3:
#                     tags.append(AssTagOutlineAlpha(alpha_arg))
#                 elif i == 4:
#                     tags.append(AssTagBackgroundAlpha(alpha_arg))

#         elif cmd == "alpha":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagAlpha())
#             else:
#                 tags.append(AssTagAlpha(int_to_int32(hex_str_to_int(p))))
#         elif cmd == "an":
#             n = int_str_to_int(p)

#             try:
#                 tag = AssTagAlignment(n)

#                 if any(isinstance(x, AssTagAlignment) for x in tags):
#                     tags.append(AssInvalidTagAlignment())
#                 else:
#                     tags.append(tag)
#             except:
#                 tags.append(AssInvalidTagAlignment())

#         elif cmd == "a":
#             n = int_str_to_int(p)

#             try:
#                 tag = AssTagAlignment(n, True)

#                 if any(isinstance(x, AssTagAlignment) for x in tags):
#                     tags.append(AssInvalidTagAlignment(True))
#                 else:
#                     tags.append(tag)
#             except:
#                 tags.append(AssInvalidTagAlignment(True))
#         elif cmd == "blur":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagBlurEdgesGauss())
#             else:
#                 tags.append(AssTagBlurEdgesGauss(float_str_to_float(p)))

#         elif cmd == "bord":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagBorder())
#             else:
#                 tags.append(AssTagBorder(float_str_to_float(p)))

#         elif cmd == "be":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagBlurEdges())
#             else:
#                 tags.append(AssTagBlurEdges(float_str_to_float(p)))

#         elif cmd == "b":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagBold())
#             else:
#                 try:
#                     weight = int_str_to_int(p)
#                     tags.append(AssTagBold(weight))
#                 except:
#                     tags.append(AssInvalidTagBold())

#         elif cmd.startswith("clip") or cmd.startswith("iclip"):

#             inverse = cmd == "iclip"

#             if len(params) == 1:
#                 # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l522
#                 raise Exception("Not implemented")
#             elif len(params) == 2:
#                 raise Exception("Not implemented")
#             elif len(params) == 4:
#                 x0 = int_str_to_int(params[0])
#                 y0 = int_str_to_int(params[1])
#                 x1 = int_str_to_int(params[2])
#                 y1 = int_str_to_int(params[3])

#                 tags.append(AssTagClipRectangle(x0, y0, x1, y1, inverse))
#         elif cmd == "c":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagPrimaryColor(True))
#             else:
#                 red, green, blue = color_arg(int_to_int32(hex_str_to_int(p)))
#                 tags.append(AssTagPrimaryColor(red, green, blue, True))

#         elif cmd in ("fade", "fad"):
#             # // {\fade(a1=param[0], a2=param[1], a3=param[2], t1=t[0], t2=t[1], t3=t[2], t4=t[3])
#             if len(params) == 7:
#                 a1 = int_str_to_int(params[0])
#                 a2 = int_str_to_int(params[1])
#                 a3 = int_str_to_int(params[2])
#                 t1 = int_str_to_int(params[3])
#                 t2 = int_str_to_int(params[4])
#                 t3 = int_str_to_int(params[5])
#                 t4 = int_str_to_int(params[6])
#                 tags.append(AssTagFadeComplex(a1, a2, a3, t1, t2, t3, t4))
#             elif len(params) == 2:
#                 t1 = int_str_to_int(params[0])
#                 t2 = int_str_to_int(params[1])
#                 tags.append(AssTagFade(t1, t2))
#         elif cmd == "fax":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagXShear())
#             else:
#                 tags.append(AssTagXShear(float_str_to_float(p)))
#         elif cmd == "fay":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagYShear())
#             else:
#                 tags.append(AssTagYShear(float_str_to_float(p)))
#         elif cmd == "fe":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagFontEncoding())
#             else:
#                 tags.append(AssTagFontEncoding(int_str_to_int(p)))

#         elif cmd == "fn":
#             # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l1683
#             if len(p) == 0 and p == "0":
#                 tags.append(AssInvalidTagFontEncoding())
#             else:
#                 tags.append(AssTagFontName(p))

#         elif cmd == "frx":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagXRotation())
#             else:
#                 tags.append(AssTagXRotation(float_str_to_float(p)))
#         elif cmd == "fry":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagYRotation())
#             else:
#                 tags.append(AssTagYRotation(float_str_to_float(p)))
#         elif cmd == "frz":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagZRotation())
#             else:
#                 tags.append(AssTagZRotation(float_str_to_float(p)))
#         elif cmd == "fr":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagZRotation(True))
#             else:
#                 tags.append(AssTagZRotation(float_str_to_float(p), True))

#         elif cmd == "fscx":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagFontXScale())
#             else:
#                 tags.append(AssTagFontXScale(float_str_to_float(p)))

#         elif cmd == "fscy":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagFontYScale())
#             else:
#                 tags.append(AssTagFontYScale(float_str_to_float(p)))
#         elif cmd == "fsc":

#             tags.append(AssTagFontScale(float_str_to_float(p)))
#         elif cmd == "fsp":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagLetterSpacing())
#             else:
#                 tags.append(AssTagLetterSpacing(float_str_to_float(p)))
#         elif cmd == "fs":
#             # Libass has some difference if p start with "+" or "-", but we can't mimic it
#             # https://github.com/libass/libass/blob/5f57443f1784434fe8961275da08be6d6febc688/libass/ass_parse.c#L425-L428
#             if len(p) == 0:
#                 tags.append(AssInvalidTagFontSize())
#             else:
#                 tags.append(AssTagFontSize(float_str_to_float(p)))
#         elif cmd == "i":
#             n = int_str_to_int(p)

#             if len(p) == 0 or n not in (0, 1):
#                 tags.append(AssInvalidTagItalic())
#             else:
#                 tags.append(AssTagItalic(bool(n)))

#         elif cmd in ("kt", "K"):
#             short_tag = cmd == "K"
#             n = int_str_to_int(p)

#             if len(p) == 0:
#                 n = 100

#             tags.append(AssTagKaraokeFill(n * 10, short_tag))

#         elif cmd == "ko":
#             n = int_str_to_int(p)
#             if len(p) == 0:
#                 n = 100
#             tags.append(AssTagKaraokeOutline(n * 10))

#         elif cmd == "k":

#             n = int_str_to_int(p)
#             if len(p) == 0:
#                 n = 100
#             tags.append(AssTagKaraoke(n * 10))

#         elif cmd == "move":
#             if len(params) in (4, 6) and not any(
#                 isinstance(tag, AssTagMove) for tag in tags
#             ):
#                 x1 = float_str_to_float(params[0])
#                 y1 = float_str_to_float(params[1])
#                 x2 = float_str_to_float(params[2])
#                 y2 = float_str_to_float(params[3])
#                 t1 = t2 = None
#                 if len(params) == 6:
#                     t1 = float_str_to_float(params[4])
#                     t2 = float_str_to_float(params[5])
#                 tags.append(AssTagMove(x1, y1, x2, y2, t1, t2))

#         elif cmd == "org":
#             if len(params) == 2 and not any(
#                 isinstance(tag, AssTagRotationOrigin) for tag in tags
#             ):
#                 x = float_str_to_float(params[0])
#                 y = float_str_to_float(params[1])

#                 tags.append(AssTagRotationOrigin(x, y))

#         elif cmd == "pbo":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagBaselineOffset())
#             else:
#                 tags.append(AssTagBaselineOffset(float_str_to_float(p)))
#         elif cmd == "pos":
#             if len(params) == 2 and not any(
#                 isinstance(tag, AssTagPosition) for tag in tags
#             ):
#                 x = float_str_to_float(params[0])
#                 y = float_str_to_float(params[1])

#                 tags.append(AssTagPosition(x, y))

#         elif cmd == "p":
#             tags.append(AssTagDraw(int_str_to_int(p)))

#         elif cmd == "q":
#             try:
#                 wrap_style = WrapStyle(int_str_to_int(p))
#             except:
#                 wrap_style = WrapStyle(0)

#             tags.append(AssTagWrapStyle(wrap_style))

#         elif cmd == "r":
#             tags.append(AssTagResetStyle(None if len(p) == 0 else p))
#         elif cmd == "shad":

#             if len(p) == 0:
#                 tags.append(AssInvalidTagShadow())
#             else:
#                 tags.append(AssTagShadow(float_str_to_float(p)))

#         elif cmd == "s":
#             n = int_str_to_int(p)

#             if len(p) == 0 or n not in (0, 1):
#                 tags.append(AssInvalidTagStrikeout())
#             else:
#                 tags.append(AssTagStrikeout(bool(n)))

#         elif cmd == "t":
#             p = ""

#             m_animStart = m_animEnd = None
#             m_animAccel = None

#             if len(params) == 1:
#                 p = params[0]
#             elif len(params) == 2:
#                 m_animAccel = float_str_to_float(params[0])
#                 p = params[1]
#             elif len(params) == 3:
#                 m_animStart = int_str_to_int(params[0])
#                 m_animEnd = int_str_to_int(params[0])
#                 p = params[2]
#             elif len(params) == 4:
#                 m_animStart = int_str_to_int(params[0])
#                 m_animEnd = int_str_to_int(params[0])
#                 m_animAccel = float_str_to_float(params[0])
#                 p = params[3]

#             tags = parse_tags(p, pwr, nested)

#             tags.append(
#                 AssTagAnimation(tags, m_animStart, m_animEnd, m_animAccel)
#             )
#         elif cmd == "u":
#             n = int_str_to_int(p)

#             if len(p) == 0 or n not in (0, 1):
#                 tags.append(AssInvalidTagUnderline())
#             else:
#                 tags.append(AssTagUnderline(bool(n)))
#         elif cmd == "xbord":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagXBorder())
#             else:
#                 tags.append(AssTagXBorder(float_str_to_float(p)))
#         elif cmd == "xshad":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagXShadow())
#             else:
#                 tags.append(AssTagXShadow(float_str_to_float(p)))

#         elif cmd == "ybord":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagYBorder())
#             else:
#                 tags.append(AssTagYBorder(float_str_to_float(p)))
#         elif cmd == "yshad":
#             if len(p) == 0:
#                 tags.append(AssInvalidTagYShadow())
#             else:
#                 tags.append(AssTagYShadow(float_str_to_float(p)))

#         i = j
#     return tags


# def parse_ass(text: str) -> list[AssItem]:
#     # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_render.c#L2044-L2064
#     ass_items = []

#     i = 0
#     while i < len(text):

#         find_left_bracket_index = text.find("{", i)

#         if find_left_bracket_index == -1:
#             # There is no tag to parse
#             ass_text = AssText(text[i:])
#             ass_items.append(ass_text)

#             i = len(text)

#         else:
#             # There can be a tag to parse
#             # Ex:
#             #    - This is a{n example
#             #    - This is a{\\b1}n example

#             find_right_bracket_index = text.find("}", find_left_bracket_index)

#             if find_right_bracket_index == -1:
#                 # There is no tag to parse
#                 # Ex: This is a{n example

#                 ass_text = AssText(text[i:])
#                 ass_items.append(ass_text)

#                 i = len(text)

#             else:
#                 # There is a tag to parse
#                 # Ex: This is a{\\b1}n example

#                 if i < find_left_bracket_index:
#                     # There is some text to parse before the {
#                     # Ex: This is a{\\b1}
#                     ass_text = AssText(text[i:find_left_bracket_index])
#                     ass_items.append(ass_text)

#                 tag_list_opening = AssTagListOpening()
#                 ass_items.append(tag_list_opening)

#                 ass_items.extend(
#                     parse_tags(
#                         text[
#                             find_left_bracket_index
#                             + 1 : find_right_bracket_index
#                         ],
#                         1,
#                         False,
#                     )
#                 )

#                 tag_list_ending = AssTagListEnding()
#                 ass_items.append(tag_list_ending)

#                 i = find_right_bracket_index + 1

#     return ass_items


# """def parse_ass(text: str) -> List[AssItem]:
#     # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l2153
#     ass_items = []

#     ass_items.append(AssTagListOpening())

#     while len(text) != 0:
#         print(text)
#         if text[0] == '{' and (i := text.find("}")) > 0:
#             ass_items.append(AssTagListOpening())

#             ass_items.append(parse_tags(text[1:i], 1, False))

#             ass_items.append(AssTagListEnding())

#             print(i)
#             print(text[i+1:])
            
#             text = text[i+1:]
#         else:
#             bracket_index = text.find("{")

#             if bracket_index == -1:
#                 ass_items.append(AssText(text))
#                 text = ""

#     ass_items.append(AssTagListEnding())


#     return ass_items
# """


# def tags_to_line(tags: List[AssTag]):
#     return "".join(str(tag) for tag in tags)


# @cache
# def ass_to_plaintext(text: str) -> str:
#     """Strip ASS tags from an ASS line.

#     :param text: input ASS line
#     :return: plain text
#     """
#     try:
#         ass_line = parse_ass(text)
#     except ParseError:
#         ret = str(re.sub("{[^}]*}", "", text))
#     else:
#         ret = ""
#         for item in ass_line:
#             if isinstance(item, AssText):
#                 ret += item.text
#     return ret.replace("\\h", " ").replace("\\n", " ").replace("\\N", "\n")
