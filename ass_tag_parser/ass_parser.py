from typing import List

from ass_tag_parser.ass_item import (
    AssTagAlignment,
)
from ass_tag_parser.ass_item.ass_tag_alignment import Alignment, LegacyAlignment
from ass_tag_parser.ass_item.ass_tag_general import AssTagRotationOrigin
from ass_tag_parser.ass_item.ass_tag_position import AssTagMove, AssTagPosition
from ass_tag_parser.ass_item.ass_tag_wrap_style import WrapStyle
from ass_tag_parser.ass_item.ass_valid_tag import (
    AssValidTagAlignment,
    AssValidTagAlpha,
    AssValidTagAnimation,
    AssValidTagBackgroundAlpha,
    AssValidTagBackgroundColor,
    AssValidTagBaselineOffset,
    AssValidTagBlurEdges,
    AssValidTagBlurEdgesGauss,
    AssValidTagBold,
    AssValidTagBorder,
    AssValidTagClipRectangle,
    AssValidTagClipVector,
    AssValidTagDraw,
    AssValidTagFade,
    AssValidTagFadeComplex,
    AssValidTagFontEncoding,
    AssValidTagFontName,
    AssValidTagFontScale,
    AssValidTagFontSize,
    AssValidTagFontXScale,
    AssValidTagFontYScale,
    AssValidTagItalic,
    AssValidTagKaraoke,
    AssValidTagKaraokeFill,
    AssValidTagKaraokeOutline,
    AssValidTagLetterSpacing,
    AssValidTagMove,
    AssValidTagOutlineAlpha,
    AssValidTagOutlineColor,
    AssValidTagPosition,
    AssValidTagPrimaryAlpha,
    AssValidTagPrimaryColor,
    AssValidTagResetStyle,
    AssValidTagRotationOrigin,
    AssValidTagSecondaryAlpha,
    AssValidTagSecondaryColor,
    AssValidTagShadow,
    AssValidTagStrikeout,
    AssValidTagUnderline,
    AssValidTagWrapStyle,
    AssValidTagXBorder,
    AssValidTagXRotation,
    AssValidTagXShadow,
    AssValidTagXShear,
    AssValidTagYBorder,
    AssValidTagYRotation,
    AssValidTagYShadow,
    AssValidTagYShear,
    AssValidTagZRotation,
)
from ass_tag_parser.ass_item.ass_invalid_tag import (
    AssInvalidTagAlignment,
    AssInvalidTagAlpha,
    AssInvalidTagAnimation,
    AssInvalidTagBackgroundAlpha,
    AssInvalidTagBackgroundColor,
    AssInvalidTagBaselineOffset,
    AssInvalidTagBlurEdges,
    AssInvalidTagBlurEdgesGauss,
    AssInvalidTagBold,
    AssInvalidTagBorder,
    AssInvalidTagClipRectangle,
    AssInvalidTagClipVector,
    AssInvalidTagDraw,
    AssInvalidTagFade,
    AssInvalidTagFadeComplex,
    AssInvalidTagFontEncoding,
    AssInvalidTagFontName,
    AssInvalidTagFontScale,
    AssInvalidTagFontSize,
    AssInvalidTagFontXScale,
    AssInvalidTagFontYScale,
    AssInvalidTagItalic,
    AssInvalidTagKaraoke,
    AssInvalidTagKaraokeFill,
    AssInvalidTagKaraokeOutline,
    AssInvalidTagLetterSpacing,
    AssInvalidTagMove,
    AssInvalidTagOutlineAlpha,
    AssInvalidTagOutlineColor,
    AssInvalidTagPosition,
    AssInvalidTagPrimaryAlpha,
    AssInvalidTagPrimaryColor,
    AssInvalidTagResetStyle,
    AssInvalidTagRotationOrigin,
    AssInvalidTagSecondaryAlpha,
    AssInvalidTagSecondaryColor,
    AssInvalidTagShadow,
    AssInvalidTagStrikeout,
    AssInvalidTagUnderline,
    AssInvalidTagWrapStyle,
    AssInvalidTagXBorder,
    AssInvalidTagXRotation,
    AssInvalidTagXShadow,
    AssInvalidTagXShear,
    AssInvalidTagYBorder,
    AssInvalidTagYRotation,
    AssInvalidTagYShadow,
    AssInvalidTagYShear,
    AssInvalidTagZRotation,
)
from ass_tag_parser.ass_item.ass_item import (
    AssItem,
    AssTag,
    AssTagListEnding,
    AssTagListOpening,
    AssText,
)


from ass_tag_parser.ass_type_parser import TypeParser


def parse_tags(text: str) -> List[AssTag]:
    # https://github.com/libass/libass/blob/5f57443f1784434fe8961275da08be6d6febc688/libass/ass_parse.c#L242-L869
    # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l1383
    tags: List[AssTag] = []
    i = 0

    while (j := text.find("\\", i)) >= 0:
        # Skip the \
        j += 1

        cmd: str = ""
        for c in text[j:]:
            if c in ("(", "\\"):
                break
            else:
                cmd += c
                j += 1

        cmd = TypeParser.strip_whitespace(cmd)

        if len(cmd) == 0:
            i = j
            continue

        params: List[str] = []

        # TODO Voir si retirer j < len(text)
        if j < len(text) and text[j] == "(":

            param: str = ""
            # Skip the (
            j += 1
            for c in text[j:]:
                if c == ")":
                    break
                else:
                    param += c
                    j += 1

            param = TypeParser.strip_whitespace(param)

            temp_j = j

            while len(param) != 0:
                i = param.find(",")
                j = param.find("\\")

                if i >= 0 and (j < 0 or i < j):
                    s = TypeParser.strip_whitespace(param[:i])
                    if len(s) != 0:
                        params.append(s)
                    param = param[i + 1 :] if i + 1 < len(param) else ""
                else:
                    param = TypeParser.strip_whitespace(param)
                    if len(param) != 0:
                        params.append(param)
                    param = ""

            j = temp_j

        if cmd.startswith(("1c", "2c", "3c", "4c")):
            params.append(cmd[2:].strip("&H"))
            cmd = cmd[:2]
        elif cmd.startswith(("1a", "2a", "3a", "4a")):
            params.append(cmd[2:].strip("&H"))
            cmd = cmd[:2]
        elif cmd.startswith("alpha"):
            params.append(cmd[5:].strip("&H"))
            cmd = cmd[:5]
        elif cmd.startswith("an"):
            params.append(cmd[2:])
            cmd = cmd[:2]
        elif cmd.startswith("a"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith("blur"):
            params.append(cmd[4:])
            cmd = cmd[:4]
        elif cmd.startswith("bord"):
            params.append(cmd[4:])
            cmd = cmd[:4]
        elif cmd.startswith("be"):
            params.append(cmd[2:])
            cmd = cmd[:2]
        elif cmd.startswith("b"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith("clip"):
            pass
        elif cmd.startswith("c"):
            params.append(cmd[1:].strip("&H"))
            cmd = cmd[:1]
        elif cmd.startswith("fade"):
            pass
        elif cmd.startswith("fe"):
            params.append(cmd[2:])
            cmd = cmd[:2]
        elif cmd.startswith("fn"):
            params.append(cmd[2:])
            cmd = cmd[:2]
        elif cmd.startswith(("frx", "fry", "frz")):
            params.append(cmd[3:])
            cmd = cmd[:3]
        elif cmd.startswith(("fax", "fay")):
            params.append(cmd[3:])
            cmd = cmd[:3]
        elif cmd.startswith("fr"):
            params.append(cmd[2:])
            cmd = cmd[:2]
        elif cmd.startswith(("fscx", "fscy")):
            params.append(cmd[4:])
            cmd = cmd[:4]
        elif cmd.startswith("fsc"):
            params.append(cmd[3:])
            cmd = cmd[:3]
        elif cmd.startswith("fsp"):
            params.append(cmd[3:])
            cmd = cmd[:3]
        elif cmd.startswith("fs"):
            params.append(cmd[2:])
            cmd = cmd[:2]
        elif cmd.startswith("iclip"):
            pass
        elif cmd.startswith("i"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith(("kt", "kf", "ko")):
            params.append(cmd[2:])
            cmd = cmd[:2]
        elif cmd.startswith(("k", "K")):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith("move"):
            pass
        elif cmd.startswith("org"):
            pass
        elif cmd.startswith("pbo"):
            params.append(cmd[3:])
            cmd = cmd[:3]
        elif cmd.startswith("pos"):
            pass
        elif cmd.startswith("p"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith("q"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith("r"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith("shad"):
            params.append(cmd[4:])
            cmd = cmd[:4]
        elif cmd.startswith("s"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith("t"):
            pass
        elif cmd.startswith("u"):
            params.append(cmd[1:])
            cmd = cmd[:1]
        elif cmd.startswith(("xbord", "xshad", "ybord", "yshad")):
            params.append(cmd[5:])
            cmd = cmd[:5]

        p = params[0] if len(params) > 0 else ""

        if cmd in ("1c", "2c", "3c", "4c"):
            i = ord(cmd[0]) - ord("0")

            if len(p) == 0:
                if i == 1:
                    tags.append(AssInvalidTagPrimaryColor(p, False))
                elif i == 2:
                    tags.append(AssInvalidTagSecondaryColor(p))
                elif i == 3:
                    tags.append(AssInvalidTagOutlineColor(p))
                elif i == 4:
                    tags.append(AssInvalidTagBackgroundColor(p))
            else:

                red, green, blue = TypeParser.color_arg(TypeParser.hex_str_to_int(p))

                if i == 1:
                    tags.append(AssValidTagPrimaryColor(False, red, green, blue))
                elif i == 2:
                    tags.append(AssValidTagSecondaryColor(red, green, blue))
                elif i == 3:
                    tags.append(AssValidTagOutlineColor(red, green, blue))
                elif i == 4:
                    tags.append(AssValidTagBackgroundColor(red, green, blue))

        elif cmd in ("1a", "2a", "3a", "4a"):
            i = ord(cmd[0]) - ord("0")

            if len(p) == 0:
                if i == 1:
                    tags.append(AssInvalidTagPrimaryAlpha(p))
                elif i == 2:
                    tags.append(AssInvalidTagSecondaryAlpha(p))
                elif i == 3:
                    tags.append(AssInvalidTagOutlineAlpha(p))
                elif i == 4:
                    tags.append(AssInvalidTagBackgroundAlpha(p))
            else:

                alpha = TypeParser.hex_str_to_int(p)

                if i == 1:
                    tags.append(AssValidTagPrimaryAlpha(alpha))
                elif i == 2:
                    tags.append(AssValidTagSecondaryAlpha(alpha))
                elif i == 3:
                    tags.append(AssValidTagOutlineAlpha(alpha))
                elif i == 4:
                    tags.append(AssValidTagBackgroundAlpha(alpha))

        elif cmd == "alpha":
            if len(p) == 0:
                tags.append(AssInvalidTagAlpha(p))
            else:
                tags.append(AssValidTagAlpha(TypeParser.hex_str_to_int(p)))
        elif cmd == "an":
            try:
                an_tag = AssValidTagAlignment(Alignment(TypeParser.int_str_to_int(p)))
            except:
                an_tag = AssInvalidTagAlignment(p, False)

            if not any(isinstance(tag, AssTagAlignment) for tag in tags):
                tags.append(an_tag)

        elif cmd == "a":
            try:
                an_tag = AssValidTagAlignment(
                    LegacyAlignment(TypeParser.int_str_to_int(p)), True
                )
            except:
                an_tag = AssInvalidTagAlignment(p, True)

            if not any(isinstance(tag, AssTagAlignment) for tag in tags):
                tags.append(an_tag)

        elif cmd == "blur":
            if len(p) == 0:
                tags.append(AssInvalidTagBlurEdgesGauss(p))
            else:
                tags.append(AssValidTagBlurEdgesGauss(TypeParser.float_str_to_float(p)))

        elif cmd == "bord":
            if len(p) == 0:
                tags.append(AssInvalidTagBorder(p))
            else:
                tags.append(AssValidTagBorder(TypeParser.float_str_to_float(p)))

        elif cmd == "be":
            if len(p) == 0:
                tags.append(AssInvalidTagBlurEdges(p))
            else:
                tags.append(AssValidTagBlurEdges(TypeParser.float_str_to_float(p)))

        elif cmd == "b":
            if len(p) == 0:
                tags.append(AssInvalidTagBold(p))
            else:
                try:
                    tags.append(AssValidTagBold(TypeParser.int_str_to_int(p)))
                except:
                    tags.append(AssInvalidTagBold(p))

        elif cmd in ("clip", "iclip"):

            invert = cmd == "iclip"

            if len(params) == 1:
                # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l522
                raise Exception("Not implemented")
            elif len(params) == 2:
                raise Exception("Not implemented")
            elif len(params) == 4:
                x1 = TypeParser.int_str_to_int(params[0])
                y1 = TypeParser.int_str_to_int(params[1])
                x2 = TypeParser.int_str_to_int(params[2])
                y2 = TypeParser.int_str_to_int(params[3])

                tags.append(AssValidTagClipRectangle(invert, x1, y1, x2, y2))
        elif cmd == "c":
            if len(p) == 0:
                tags.append(AssInvalidTagPrimaryColor(p, True))
            else:
                red, green, blue = TypeParser.color_arg((TypeParser.hex_str_to_int(p)))
                tags.append(AssValidTagPrimaryColor(True, red, green, blue))

        elif cmd in ("fade", "fad"):
            # // {\fade(a1=param[0], a2=param[1], a3=param[2], t1=t[0], t2=t[1], t3=t[2], t4=t[3])
            if len(params) == 7:
                a1 = TypeParser.int_str_to_int(params[0])
                a2 = TypeParser.int_str_to_int(params[1])
                a3 = TypeParser.int_str_to_int(params[2])
                t1 = TypeParser.int_str_to_int(params[3])
                t2 = TypeParser.int_str_to_int(params[4])
                t3 = TypeParser.int_str_to_int(params[5])
                t4 = TypeParser.int_str_to_int(params[6])
                tags.append(AssValidTagFadeComplex(a1, a2, a3, t1, t2, t3, t4))
            elif len(params) == 2:
                t1 = TypeParser.int_str_to_int(params[0])
                t2 = TypeParser.int_str_to_int(params[1])
                tags.append(AssValidTagFade(t1, t2))
        elif cmd == "fax":
            if len(p) == 0:
                tags.append(AssInvalidTagXShear(p))
            else:
                tags.append(AssValidTagXShear(TypeParser.float_str_to_float(p)))
        elif cmd == "fay":
            if len(p) == 0:
                tags.append(AssInvalidTagYShear(p))
            else:
                tags.append(AssValidTagYShear(TypeParser.float_str_to_float(p)))
        elif cmd == "fe":
            if len(p) == 0:
                tags.append(AssInvalidTagFontEncoding(p))
            else:
                tags.append(AssValidTagFontEncoding(TypeParser.int_str_to_int(p)))

        elif cmd == "fn":
            # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l1683
            if len(p) == 0 or p == "0":
                tags.append(AssInvalidTagFontName(p))
            else:
                tags.append(AssValidTagFontName(p))

        elif cmd == "frx":
            if len(p) == 0:
                tags.append(AssInvalidTagXRotation(p))
            else:
                tags.append(AssValidTagXRotation(TypeParser.float_str_to_float(p)))
        elif cmd == "fry":
            if len(p) == 0:
                tags.append(AssInvalidTagYRotation(p))
            else:
                tags.append(AssValidTagYRotation(TypeParser.float_str_to_float(p)))
        elif cmd == "frz":
            if len(p) == 0:
                tags.append(AssInvalidTagZRotation(p))
            else:
                tags.append(
                    AssValidTagZRotation(False, TypeParser.float_str_to_float(p))
                )
        elif cmd == "fr":
            if len(p) == 0:
                tags.append(AssInvalidTagZRotation(True))
            else:
                tags.append(
                    AssValidTagZRotation(True, TypeParser.float_str_to_float(p))
                )

        elif cmd == "fscx":
            if len(p) == 0:
                tags.append(AssInvalidTagFontXScale(p))
            else:
                tags.append(AssValidTagFontXScale(TypeParser.float_str_to_float(p)))

        elif cmd == "fscy":
            if len(p) == 0:
                tags.append(AssInvalidTagFontYScale(p))
            else:
                tags.append(AssValidTagFontYScale(TypeParser.float_str_to_float(p)))
        elif cmd == "fsc":
            tags.append(AssValidTagFontScale())
        elif cmd == "fsp":
            if len(p) == 0:
                tags.append(AssInvalidTagLetterSpacing(p))
            else:
                tags.append(AssValidTagLetterSpacing(TypeParser.float_str_to_float(p)))
        elif cmd == "fs":
            if len(p) == 0:
                tags.append(AssInvalidTagFontSize(p))
            else:
                tags.append(AssValidTagFontSize(TypeParser.float_str_to_float(p)))
        elif cmd == "i":
            n = TypeParser.int_str_to_int(p)

            if len(p) == 0 or n not in (0, 1):
                tags.append(AssInvalidTagItalic(p))
            else:
                tags.append(AssValidTagItalic(bool(n)))

        elif cmd in ("kf", "K"):
            short_tag = cmd == "K"
            n = TypeParser.float_str_to_float(p)

            if len(p) == 0:
                n = 100

            tags.append(AssValidTagKaraokeFill(n * 10, short_tag))

        elif cmd == "ko":
            n = TypeParser.float_str_to_float(p)

            if len(p) == 0:
                n = 100

            tags.append(AssValidTagKaraokeOutline(n * 10))

        elif cmd == "k":
            n = TypeParser.float_str_to_float(p)

            if len(p) == 0:
                n = 100

            tags.append(AssValidTagKaraoke(n * 10))

        elif cmd == "move":
            if len(params) in (4, 6) and not any(
                isinstance(tag, AssTagMove) for tag in tags
            ):
                x1 = TypeParser.float_str_to_float(params[0])
                y1 = TypeParser.float_str_to_float(params[1])
                x2 = TypeParser.float_str_to_float(params[2])
                y2 = TypeParser.float_str_to_float(params[3])
                t1 = t2 = None
                if len(params) == 6:
                    t1 = TypeParser.int_str_to_int(params[4])
                    t2 = TypeParser.int_str_to_int(params[5])
                tags.append(AssValidTagMove(x1, y1, x2, y2, t1, t2))

        elif cmd == "org":
            if len(params) == 2 and not any(
                isinstance(tag, AssTagRotationOrigin) for tag in tags
            ):
                x = TypeParser.float_str_to_float(params[0])
                y = TypeParser.float_str_to_float(params[1])

                tags.append(AssValidTagRotationOrigin(x, y))

        elif cmd == "pbo":
            tags.append(AssValidTagBaselineOffset(TypeParser.float_str_to_float(p)))
        elif cmd == "pos":
            if len(params) == 2 and not any(
                isinstance(tag, AssTagPosition) for tag in tags
            ):
                x = TypeParser.float_str_to_float(params[0])
                y = TypeParser.float_str_to_float(params[1])

                tags.append(AssValidTagPosition(x, y))

        elif cmd == "p":
            tags.append(AssValidTagDraw(TypeParser.int_str_to_int(p)))

        elif cmd == "q":
            if len(p) == 0:
                tags.append(AssInvalidTagWrapStyle(p))
            else:
                try:
                    tags.append(
                        AssValidTagWrapStyle(WrapStyle(TypeParser.int_str_to_int(p)))
                    )
                except:
                    tags.append(AssInvalidTagWrapStyle(p))

        elif cmd == "r":
            tags.append(AssValidTagResetStyle(None if len(p) == 0 else p))

        elif cmd == "shad":
            if len(p) == 0:
                tags.append(AssInvalidTagShadow(p))
            else:
                tags.append(AssValidTagShadow(TypeParser.float_str_to_float(p)))

        elif cmd == "s":
            n = TypeParser.int_str_to_int(p)

            if len(p) == 0 or n not in (0, 1):
                tags.append(AssInvalidTagStrikeout())
            else:
                tags.append(AssValidTagStrikeout(bool(n)))

        elif cmd == "t":
            p = ""

            m_animStart = m_animEnd = None
            m_animAccel = 1.0

            if len(params) == 1:
                p = params[0]
            elif len(params) == 2:
                m_animAccel = TypeParser.float_str_to_float(params[0])
                p = params[1]
            elif len(params) == 3:
                m_animStart = TypeParser.int_str_to_int(params[0])
                m_animEnd = TypeParser.int_str_to_int(params[1])
                p = params[2]
            elif len(params) == 4:
                m_animStart = TypeParser.int_str_to_int(params[0])
                m_animEnd = TypeParser.int_str_to_int(params[1])
                m_animAccel = TypeParser.float_str_to_float(params[2])
                p = params[3]

            t_tags = parse_tags(p)

            # TODO Verify recursivity
            tags.append(AssValidTagAnimation(t_tags, m_animAccel, m_animStart, m_animEnd))
        elif cmd == "u":
            n = TypeParser.int_str_to_int(p)

            if len(p) == 0 or n not in (0, 1):
                tags.append(AssInvalidTagUnderline(p))
            else:
                tags.append(AssValidTagUnderline(bool(n)))
        elif cmd == "xbord":
            if len(p) == 0:
                tags.append(AssInvalidTagXBorder(p))
            else:
                tags.append(AssValidTagXBorder(TypeParser.float_str_to_float(p)))
        elif cmd == "xshad":
            if len(p) == 0:
                tags.append(AssInvalidTagXShadow(p))
            else:
                tags.append(AssValidTagXShadow(TypeParser.float_str_to_float(p)))

        elif cmd == "ybord":
            if len(p) == 0:
                tags.append(AssInvalidTagYBorder(p))
            else:
                tags.append(AssValidTagYBorder(TypeParser.float_str_to_float(p)))
        elif cmd == "yshad":
            if len(p) == 0:
                tags.append(AssInvalidTagYShadow(p))
            else:
                tags.append(AssValidTagYShadow(TypeParser.float_str_to_float(p)))

        i = j

    return tags


def parse_ass(text: str) -> List[AssItem]:
    # https://github.com/libass/libass/blob/44f6532daf5eb13cb1aa95f5449a77b5df1dd85b/libass/ass_render.c#L2044-L2064
    ass_items = []

    i = 0
    while i < len(text):

        find_left_bracket_index = text.find("{", i)

        if find_left_bracket_index == -1:
            # There is no tag to parse
            ass_text = AssText(text[i:])
            ass_items.append(ass_text)

            i = len(text)

        else:
            # There can be a tag to parse
            # Ex:
            #    - This is a{n example
            #    - This is a{\\b1}n example

            find_right_bracket_index = text.find("}", find_left_bracket_index)

            if find_right_bracket_index == -1:
                # There is no tag to parse
                # Ex: This is a{n example

                ass_text = AssText(text[i:])
                ass_items.append(ass_text)

                i = len(text)

            else:
                # There is a tag to parse
                # Ex: This is a{\\b1}n example

                if i < find_left_bracket_index:
                    # There is some text to parse before the {
                    # Ex: This is a{\\b1}
                    ass_text = AssText(text[i:find_left_bracket_index])
                    ass_items.append(ass_text)

                tag_list_opening = AssTagListOpening()
                ass_items.append(tag_list_opening)

                ass_items.extend(
                    parse_tags(
                        text[find_left_bracket_index + 1 : find_right_bracket_index],
                    )
                )

                tag_list_ending = AssTagListEnding()
                ass_items.append(tag_list_ending)

                i = find_right_bracket_index + 1

    return ass_items


"""def parse_ass(text: str) -> List[AssItem]:
    # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/RTS.cpp#l2153
    ass_items = []

    ass_items.append(AssTagListOpening())

    while len(text) != 0:
        print(text)
        if text[0] == '{' and (i := text.find("}")) > 0:
            ass_items.append(AssTagListOpening())

            ass_items.append(parse_tags(text[1:i], 1, False))

            ass_items.append(AssTagListEnding())

            print(i)
            print(text[i+1:])

            text = text[i+1:]
        else:
            bracket_index = text.find("{")

            if bracket_index == -1:
                ass_items.append(AssText(text))
                text = ""

    ass_items.append(AssTagListEnding())


    return ass_items
"""


def tags_to_text(tags: List[AssTag]):
    return "".join(str(tag) for tag in tags)
