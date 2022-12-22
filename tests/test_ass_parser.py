from typing import List

import pytest
import ass_tag_parser



@pytest.mark.parametrize(
    "text,expected_result",
    [
        ("{\\}test", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding(), ass_tag_parser.AssText("test")]),
        
        ("{\\an5}test", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlignment(ass_tag_parser.Alignment(5)), ass_tag_parser.AssTagListEnding(), ass_tag_parser.AssText("test")]),
        ("{\\an}test", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlignment("", False), ass_tag_parser.AssTagListEnding(), ass_tag_parser.AssText("test")]),
        ("{\\an0}test", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlignment("0", False), ass_tag_parser.AssTagListEnding(), ass_tag_parser.AssText("test")]),
        ("{\\an10}test", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlignment("10", False), ass_tag_parser.AssTagListEnding(), ass_tag_parser.AssText("test")]),
        ("{\\anTest}test", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlignment("Test", False), ass_tag_parser.AssTagListEnding(), ass_tag_parser.AssText("test")]),
    
        ("{\\alpha&HB4&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha&HB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alphaH&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha&hB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlpha(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlpha(""), ass_tag_parser.AssTagListEnding()]),
        
        ("{\\t(\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)]), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(4,\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], acceleration=4.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(0,1000,\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], time1=0, time2=1000), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(0,1000,4,\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], acceleration=4.0, time1=0, time2=1000), ass_tag_parser.AssTagListEnding()]),
        ("{\\t}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([]), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(0,1000,\\be20,20,20,202,202,20,20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], time1=0, time2=1000), ass_tag_parser.AssTagListEnding()]),

    ],
)
def test_parse_tag(text: str, expected_result: List[ass_tag_parser.AssItem]):
    assert ass_tag_parser.parse_ass(text) == expected_result