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
            
        ("{\\t(\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)]), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(4,\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], acceleration=4.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(0,1000,\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], time1=0, time2=1000), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(0,1000,4,\\be20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], acceleration=4.0, time1=0, time2=1000), ass_tag_parser.AssTagListEnding()]),
        ("{\\t}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([]), ass_tag_parser.AssTagListEnding()]),
        ("{\\t(0,1000,\\be20,20,20,202,202,20,20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAnimation([ass_tag_parser.AssValidTagBlurEdges(20.0)], time1=0, time2=1000), ass_tag_parser.AssTagListEnding()]),

        ("{\\alpha&HB4&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha&HB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alphaH&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha&hB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlpha(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\alpha  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagAlpha(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\1a&HB4&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\1a&HB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\1aH&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\1a&hB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryAlpha(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\1a&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\1a}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagPrimaryAlpha(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\1a  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagPrimaryAlpha(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\2a&HB4&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\2a&HB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\2aH&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\2a&hB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryAlpha(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\2a&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\2a}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagSecondaryAlpha(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\2a  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagSecondaryAlpha(""), ass_tag_parser.AssTagListEnding()]),



        ("{\\3a&HB4&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\3a&HB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\3aH&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\3a&hB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineAlpha(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\3a&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\3a}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagOutlineAlpha(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\3a  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagOutlineAlpha(""), ass_tag_parser.AssTagListEnding()]),


        ("{\\4a&HB4&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\4a&HB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\4aH&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\4a&hB4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundAlpha(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\4a&B4}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundAlpha(180), ass_tag_parser.AssTagListEnding()]),
        ("{\\4a}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagBackgroundAlpha(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\4a  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagBackgroundAlpha(""), ass_tag_parser.AssTagListEnding()]),


        ("{\\1c&H6465D9&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(False, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\1c&H6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(False, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\1cH&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(False, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\1c&h6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(False, 0, 0, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\1c&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(False, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\1c}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagPrimaryColor("", False), ass_tag_parser.AssTagListEnding()]),
        ("{\\1c  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagPrimaryColor("", False), ass_tag_parser.AssTagListEnding()]),

        ("{\\c&H6465D9&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(True, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\c&H6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(True, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\cH&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(True, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\c&h6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(True, 0, 0, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\c&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPrimaryColor(True, 217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\c}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagPrimaryColor("", True), ass_tag_parser.AssTagListEnding()]),
        ("{\\c  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagPrimaryColor("", True), ass_tag_parser.AssTagListEnding()]),


        ("{\\2c&H6465D9&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\2c&H6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\2cH&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\2c&h6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryColor(0, 0, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\2c&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagSecondaryColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\2c}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagSecondaryColor(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\2c  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagSecondaryColor(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\3c&H6465D9&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\3c&H6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\3cH&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\3c&h6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineColor(0, 0, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\3c&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagOutlineColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\3c}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagOutlineColor(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\3c  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagOutlineColor(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\4c&H6465D9&}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\4c&H6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\4cH&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\4c&h6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundColor(0, 0, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\4c&6465D9}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBackgroundColor(217, 101, 100), ass_tag_parser.AssTagListEnding()]),
        ("{\\4c}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagBackgroundColor(""), ass_tag_parser.AssTagListEnding()]),
        ("{\\4c  }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagBackgroundColor(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\pbo4.5}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBaselineOffset(4.5), ass_tag_parser.AssTagListEnding()]),
        ("{\\pbo }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBaselineOffset(0.0), ass_tag_parser.AssTagListEnding()]),
        
        ("{\\be }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBlurEdges(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\beTest}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBlurEdges(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\beTest}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBlurEdges(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\be2.2}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBlurEdges(2.2), ass_tag_parser.AssTagListEnding()]),

        ("{\\blur }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBlurEdgesGauss(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\blurTest}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBlurEdgesGauss(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\blur2.2}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBlurEdgesGauss(2.2), ass_tag_parser.AssTagListEnding()]),

        ("{\\b0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBold(400), ass_tag_parser.AssTagListEnding()]),
        ("{\\b1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBold(700), ass_tag_parser.AssTagListEnding()]),
        ("{\\b100}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBold(100), ass_tag_parser.AssTagListEnding()]),
        ("{\\b99}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagBold("99"), ass_tag_parser.AssTagListEnding()]),
        ("{\\b }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagBold(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\bord400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagBorder(400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\bord }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagBorder(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\xbord400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagXBorder(400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\xbord }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagXBorder(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\ybord400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagYBorder(400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\ybord }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagYBorder(""), ass_tag_parser.AssTagListEnding()]),


        ("{\\clip(100,200,300,400)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagClipRectangle(False, 100, 200, 300, 400), ass_tag_parser.AssTagListEnding()]),
        ("{\\clip  (100,200,300,400)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagClipRectangle(False, 100, 200, 300, 400), ass_tag_parser.AssTagListEnding()]),
        ("{\\clip(100,200,300,400}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagClipRectangle(False, 100, 200, 300, 400), ass_tag_parser.AssTagListEnding()]),
        ("{\\iclip(100,200,300,400)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagClipRectangle(True, 100, 200, 300, 400), ass_tag_parser.AssTagListEnding()]),
        ("{\\clip100,200,300,400)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding()]),

        ("{\\p1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagDraw(1), ass_tag_parser.AssTagListEnding()]),
        ("{\\p}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagDraw(0), ass_tag_parser.AssTagListEnding()]),
        
        ("{\\fad(0, 500)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFade(0, 500), ass_tag_parser.AssTagListEnding()]),
        ("{\\fad(0, 500}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFade(0, 500), ass_tag_parser.AssTagListEnding()]),
        ("{\\fad0, 500}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding()]),

        ("{\\fade(255,0,255,0,500,1000,1500)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFadeComplex(255, 0, 255, 0, 500, 1000, 1500), ass_tag_parser.AssTagListEnding()]),
        ("{\\fade(255,0,255,0,500,1000,1500}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFadeComplex(255, 0, 255, 0, 500, 1000, 1500), ass_tag_parser.AssTagListEnding()]),
        ("{\\fade255,0,255,0,500,1000,1500)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding()]),
    
        ("{\\fe0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontEncoding(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\fe k}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontEncoding(0), ass_tag_parser.AssTagListEnding()]),
    
        ("{\\fnArial}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontName("Arial"), ass_tag_parser.AssTagListEnding()]),
        ("{\\fn Arial }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontName("Arial"), ass_tag_parser.AssTagListEnding()]),
        ("{\\fn 0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontName("0"), ass_tag_parser.AssTagListEnding()]),
        ("{\\fn0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagFontName("0"), ass_tag_parser.AssTagListEnding()]),
        ("{\\fn }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagFontName(""), ass_tag_parser.AssTagListEnding()]),
        
        ("{\\fscExample}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontScale(), ass_tag_parser.AssTagListEnding()]),
        ("{\\fsc}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontScale(), ass_tag_parser.AssTagListEnding()]),
        
        ("{\\fs20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontSize(20.1), ass_tag_parser.AssTagListEnding()]),
        ("{\\fs j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontSize(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\fs }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagFontSize(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\fscx20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontXScale(20.1), ass_tag_parser.AssTagListEnding()]),
        ("{\\fscx j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontXScale(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\fscx }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagFontXScale(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\fscy20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontYScale(20.1), ass_tag_parser.AssTagListEnding()]),
        ("{\\fscy j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagFontYScale(0.0), ass_tag_parser.AssTagListEnding()]),
        ("{\\fscy }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagFontYScale(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\i1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagItalic(True), ass_tag_parser.AssTagListEnding()]),
        ("{\\i0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagItalic(False), ass_tag_parser.AssTagListEnding()]),
        ("{\\i2}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagItalic("2"), ass_tag_parser.AssTagListEnding()]),
        ("{\\i }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagItalic(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\k20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraoke(201), ass_tag_parser.AssTagListEnding()]),
        ("{\\k j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraoke(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\k }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraoke(1000), ass_tag_parser.AssTagListEnding()]),

        ("{\\kf20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeFill(False, 201), ass_tag_parser.AssTagListEnding()]),
        ("{\\kf j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeFill(False, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\kf }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeFill(False, 1000), ass_tag_parser.AssTagListEnding()]),

        ("{\\K20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeFill(True, 201), ass_tag_parser.AssTagListEnding()]),
        ("{\\K j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeFill(True, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\K }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeFill(True, 1000), ass_tag_parser.AssTagListEnding()]),

        ("{\\ko20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeOutline(201), ass_tag_parser.AssTagListEnding()]),
        ("{\\ko j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeOutline(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\ko }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagKaraokeOutline(1000), ass_tag_parser.AssTagListEnding()]),

        ("{\\move(0.1, 5, 10, 20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagMove(0.1, 5, 10, 20), ass_tag_parser.AssTagListEnding()]),
        ("{\\move(0.1, 5, 10, 20, 30, 0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagMove(0.1, 5, 10, 20, 30, 0), ass_tag_parser.AssTagListEnding()]),
        ("{\\move0, 500}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding()]),

        ("{\\pos(0.1, 5)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPosition(0.1, 5), ass_tag_parser.AssTagListEnding()]),
        ("{\\pos(0.1, 5}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagPosition(0.1, 5), ass_tag_parser.AssTagListEnding()]),
        ("{\\pos0, 500}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding()]),

        ("{\\rDefault}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagResetStyle("Default"), ass_tag_parser.AssTagListEnding()]),
        ("{\\r Arial }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagResetStyle(" Arial"), ass_tag_parser.AssTagListEnding()]),
        ("{\\r }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagResetStyle(), ass_tag_parser.AssTagListEnding()]),

        ("{\\org(0.1, 5)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagRotationOrigin(0.1, 5), ass_tag_parser.AssTagListEnding()]),
        ("{\\org(0.1, 5, )}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagRotationOrigin(0.1, 5), ass_tag_parser.AssTagListEnding()]),
        ("{\\org(0.1, 5}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagRotationOrigin(0.1, 5), ass_tag_parser.AssTagListEnding()]),
        ("{\\org0, 500}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding()]),
        ("{\\org(0.1, 5, 20)}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssTagListEnding()]),

        ("{\\shad20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagShadow(20.1), ass_tag_parser.AssTagListEnding()]),
        ("{\\shad j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagShadow(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\shad }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagShadow(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\xshad20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagXShadow(20.1), ass_tag_parser.AssTagListEnding()]),
        ("{\\xshad j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagXShadow(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\xshad }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagXShadow(""), ass_tag_parser.AssTagListEnding()]),
        
        ("{\\yshad20.1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagYShadow(20.1), ass_tag_parser.AssTagListEnding()]),
        ("{\\yshad j}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagYShadow(0), ass_tag_parser.AssTagListEnding()]),
        ("{\\yshad }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagYShadow(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\s1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagStrikeout(True), ass_tag_parser.AssTagListEnding()]),
        ("{\\s0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagStrikeout(False), ass_tag_parser.AssTagListEnding()]),
        ("{\\s2}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagStrikeout("2"), ass_tag_parser.AssTagListEnding()]),
        ("{\\s }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagStrikeout(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\u1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagUnderline(True), ass_tag_parser.AssTagListEnding()]),
        ("{\\u0}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagUnderline(False), ass_tag_parser.AssTagListEnding()]),
        ("{\\u2}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagUnderline("2"), ass_tag_parser.AssTagListEnding()]),
        ("{\\u }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagUnderline(""), ass_tag_parser.AssTagListEnding()]),

        ("{\\q1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagWrapStyle(ass_tag_parser.WrapStyle(1)), ass_tag_parser.AssTagListEnding()]),
        ("{\\q-1}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagWrapStyle("-1"), ass_tag_parser.AssTagListEnding()]),
        ("{\\q }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagWrapStyle(""), ass_tag_parser.AssTagListEnding()]),
        
        ("{\\frx400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagXRotation(400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\frx }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagXRotation(0), ass_tag_parser.AssTagListEnding()]),

        ("{\\fry400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagYRotation(400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\fry }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagYRotation(0), ass_tag_parser.AssTagListEnding()]),

        ("{\\fr400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagZRotation(True, 400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\fr }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagZRotation("", True), ass_tag_parser.AssTagListEnding()]),

        ("{\\frz400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagZRotation(False, 400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\frz }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssInvalidTagZRotation("", False), ass_tag_parser.AssTagListEnding()]),

        ("{\\fax400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagXShear(400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\fax }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagXShear(0.0), ass_tag_parser.AssTagListEnding()]),

        ("{\\fay400.7}", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagYShear(400.7), ass_tag_parser.AssTagListEnding()]),
        ("{\\fay }", [ass_tag_parser.AssTagListOpening(), ass_tag_parser.AssValidTagYShear(0.0), ass_tag_parser.AssTagListEnding()]),
    ],
)
def test_parse_tag(text: str, expected_result: List[ass_tag_parser.AssItem]):
    assert ass_tag_parser.parse_ass(text) == expected_result