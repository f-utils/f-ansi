import re
from f_ansi.mods.color.codes_ import (
        COLORS,
        STYLES,
        REGEX_HEX,
        REGEX_RGB
)

class Is:
    @staticmethod
    def hex(value: str) -> bool:
        hex_pattern = re.compile(REGEX_HEX)
        return bool(hex_pattern.match(value))

    @staticmethod
    def rgb(value: str) -> bool:
        rgb_pattern = re.compile(REGEX_RGB)
        match = rgb_pattern.match(value)
        if match:
            r, g, b = match.groups()
            return all(0 <= int(x) <= 255 for x in (r, g, b))
        return False

    @staticmethod
    def color(value: str) -> bool:
        sanitized_value = value.strip().upper()
        return sanitized_value in COLORS

    @staticmethod
    def style(value: str) -> bool:
        sanitized_value = value.strip().upper()
        return sanitized_value in STYLES
