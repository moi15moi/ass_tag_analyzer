class Format:
    @staticmethod
    def _format_float(number: float) -> str:
        return "{:.3f}".format(number).rstrip("0").rstrip(".")

    format_float = _format_float
