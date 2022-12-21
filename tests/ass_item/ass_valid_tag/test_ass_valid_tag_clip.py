from ass_tag_parser.ass_item.ass_valid_tag.ass_valid_tag_clip import (
    AssValidTagClipRectangle,
    AssValidTagClipVector,
)


def test_ass_valid_tag_clip_rectangle():

    assert str(AssValidTagClipRectangle(True, 20, 20, 20, 20)) == "\\iclip(20,20,20,20)"
    assert str(AssValidTagClipRectangle(False, 20, 20, 20, 20)) == "\\clip(20,20,20,20)"


def test_ass_valid_tag_clip_vector():

    assert False
