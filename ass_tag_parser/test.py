
from ass_tag_parser.ass_item import AssTagBlurEdgesGauss
from ass_tag_parser.ass_item.ass_item import AssItem
from ass_tag_parser.ass_item.ass_valid_tag import AssValidTagAnimation, AssValidTagBlurEdges
from ass_tag_parser.ass_item.ass_valid_tag.ass_valid_tag_clip import AssValidTagClipRectangle
from ass_tag_parser.ass_item.ass_invalid_tag import AssInvalidTagBlurEdgesGauss

print(AssValidTagClipRectangle(True, 20, 30, 40, 50))
print(AssValidTagAnimation([AssValidTagBlurEdges(20)], time1=20, time2=40))
print(isinstance(AssInvalidTagBlurEdgesGauss(), AssTagBlurEdgesGauss))


