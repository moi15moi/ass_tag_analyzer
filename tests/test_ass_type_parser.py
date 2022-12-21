from ass_tag_parser.ass_type_parser import TypeParser


def test_color_arg():
    assert TypeParser.color_arg(int("FA9632", 16)) == (50, 150, 250)


def test_float_str_to_float():

    # Whitespace and invalid text
    assert TypeParser.float_str_to_float("\t\v20.39445InvalidText") == 20.39445

    # Multiple dot
    assert TypeParser.float_str_to_float("20.39.445") == 20.39

    # Multiple +-
    assert TypeParser.float_str_to_float("+-20.39.445") == 0

    # Integer
    assert TypeParser.float_str_to_float("20") == 20

    # +-
    assert TypeParser.float_str_to_float("+20") == 20
    assert TypeParser.float_str_to_float("-20") == -20


def test_int_str_to_int():

    # Whitespace and invalid text
    assert TypeParser.int_str_to_int("\t\v20.39445InvalidText") == 20

    # Multiple dot
    assert TypeParser.int_str_to_int("20.39.445") == 20

    # Multiple +-
    assert TypeParser.int_str_to_int("+-20.39.445") == 0

    # Integer
    assert TypeParser.int_str_to_int("20") == 20

    # +-
    assert TypeParser.int_str_to_int("+20") == 20
    assert TypeParser.int_str_to_int("-20") == -20


def test_hex_str_to_int():

    # Whitespace and invalid text
    assert TypeParser.hex_str_to_int("\t\v6BInvalidText") == 107

    # Multiple dot
    assert TypeParser.hex_str_to_int("6B.39.445") == 107

    # Multiple +-
    assert TypeParser.hex_str_to_int("+-6B.39.445") == 0

    # Integer
    assert TypeParser.hex_str_to_int("6B") == 107

    # +-
    assert TypeParser.hex_str_to_int("+6B") == 107
    assert TypeParser.hex_str_to_int("-6B") == -107

    # With lowercase characters
    assert TypeParser.hex_str_to_int("-6b") == -107
