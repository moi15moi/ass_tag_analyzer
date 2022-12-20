from ass_tag_parser.ass_item.ass_valid_tag import (AssValidTagAlpha, AssValidTagPrimaryAlpha, AssValidTagSecondaryAlpha, AssValidTagOutlineAlpha, AssValidTagBackgroundAlpha)


def test_ass_valid_tag_alpha():

    assert str(AssValidTagAlpha(20)) == "\\alpha20"

assert False == True