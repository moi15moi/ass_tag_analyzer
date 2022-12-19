from dataclasses import dataclass

@dataclass
class Color():
    red: int
    green: int
    blue: int


@dataclass
class AssStyle():
    # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/STS.h#l31
    # https://sourceforge.net/p/guliverkli2/code/HEAD/tree/src/subtitles/STS.cpp#l2891
    margin_l: int = 20
    margin_r: int = 20
    margin_v: int = 20

    alignment: int = 2 # 1 - 9: as on the numpad, 0: default
    border_style: int = 0 # 0: outline, 1: opaque box

    outline_width_x, outline_width_y: float = 2.0
    shadow_depth_x, shadow_depth_y: float = 3.0
    primary_color: Color = Color(255, 255, 255)
    secondary_color: Color = Color(255, 255, 0)
    outline_color: Color = Color(0, 0, 0)
    shadow_color: Color = Color(0, 0, 0)

    primary_alpha: int = 0
    secondary_alpha: int = 0
    outline_alpha: int = 0
    shadow_alpha: int = 0x80

    charset: int = 1 # https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-one/64e2db6e-6eeb-443c-9ccf-0f72b37ba411
    fontname: str = "Arial"
    fontsize: float = 18.0
    font_scale_x, font_scale_y: float = 100.0
    font_spacing: float = 0.0
    font_weight: int = 700
    italic: bool = False
    underline: bool = False
    strikeout: bool = False
    blur: int = 0 #\be
    gaussian_blur: float = 0.0 # \blur
    font_angle_x, font_angle_y, font_angle_z: float = 0.0
    fontShiftX, fontShiftY: float = 0 # \fax, \fay
