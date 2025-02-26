from f_ansi.mods.color.codes_ import ANSI_COLORS, ANSI_STYLES
import re

class Is:
    @staticmethod
    def hex(value: str) -> bool:
        hex_pattern = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')
        return bool(hex_pattern.match(value))

    @staticmethod
    def rgb(value: str) -> bool:
        rgb_pattern = re.compile(r'^\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$')
        match = rgb_pattern.match(value)
        if match:
            r, g, b = match.groups()
            return all(0 <= int(x) <= 255 for x in (r, g, b))
        return False

    @staticmethod
    def color(value: str) -> bool:
        sanitized_value = value.strip().upper()
        return sanitized_value in ANSI_COLORS

    @staticmethod
    def style(value: str) -> bool:
        sanitized_value = value.strip().upper()
        return sanitized_value in ANSI_STYLES
