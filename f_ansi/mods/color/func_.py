from f import f
from f_ansi.mods.color.codes_ import ANSI_COLORS, ANSI_STYLES
from f_ansi.mods.is_ import Is
from f_core import typed, o

@typed
def sanitize_(name: str) -> str:
    return name.replace('_', '_').strip().upper()

f.o.i('join', 'join of types', o.join)

@typed
def color_(color_input: o.join(str, tuple), style_codes: list = []) -> tuple:
    if Is.rgb(color_input):
        if isinstance(color_input, tuple):
            r, g, b = color_input
        else:
            r, g, b = map(int, color_input.strip('()').split(','))
        rgb_color_code = f"38;2;{r};{g};{b}"
        return rgb_color_code, style_codes
    sanitized_input = sanitize_(color_input)

    if Is.color(sanitized_input):
        color_code = ANSI_COLORS[sanitized_input]
        return color_code, style_codes

    if Is.hex(color_input):
        hex_color = color_input.lstrip('#')
        lv = len(hex_color)
        rgb = tuple(int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        rgb_color_code = f"38;2;{rgb[0]};{rgb[1]};{rgb[2]}"
        return rgb_color_code, style_codes

    valid_colors = ', '.join(ANSI_COLORS.keys())
    raise ValueError(f"Invalid color input: must be a valid RGB, color name, or HEX color. "
                     f"Valid color names are: {valid_colors}")

@typed
def style_(style_inputs: tuple, style_codes: list = []) -> list:
    new_style_codes = style_codes.copy()
    for style_input in style_inputs:
        if not Is.style(style_input):
            valid_styles = ', '.join(ANSI_STYLES.keys())
            raise ValueError(f"Invalid style input: '{style_input}' is not a valid style name. "
                             f"Valid styles are: {valid_styles}")
        sanitized_input = sanitize_(style_input)
        style_code = ANSI_STYLES[sanitized_input]
        if style_code not in new_style_codes:
            new_style_codes.append(style_code)
    return new_style_codes
