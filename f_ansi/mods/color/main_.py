from f_ansi.mods.color.codes_ import COLORS, STYLES, RESET
from f_ansi.mods.color.func_ import color_, style_, sanitize_

class _Color:
    def __init__(self, color_code=None, style_codes=None):
        self.color_code = color_code
        self.style_codes = style_codes or []

    def __call__(self, text):
        ansi_seq = self.style_codes.copy()
        if self.color_code:
            ansi_seq.append(self.color_code)
        ansi_seq_str = ';'.join(ansi_seq)
        return f'\033[{ansi_seq_str}m{text}{RESET}'

    def color(self, color_input):
        color_code, _ = color_(color_input, self.style_codes)
        return _Color(color_code=color_code, style_codes=self.style_codes)

    def style(self, *style_inputs):
        new_style_codes = style_(style_inputs, self.style_codes)
        return _Color(color_code=self.color_code, style_codes=new_style_codes)

    def add_color(self, color_name):
        new_color_code = COLORS.get(sanitize_(color_name))
        return _Color(color_code=new_color_code, style_codes=self.style_codes)

    def add_style(self, style_name):
        new_style_code = STYLES.get(sanitize_(style_name))
        new_style_codes = self.style_codes.copy()
        if new_style_code not in new_style_codes:
            new_style_codes.append(new_style_code)
        return _Color(color_code=self.color_code, style_codes=new_style_codes)

    def __getattr__(self, name):
        sanitized_name = sanitize_(name)
        if sanitized_name in COLORS:
            return self.add_color(sanitized_name)
        elif sanitized_name in STYLES:
            return self.add_style(sanitized_name)
        raise AttributeError(f"'_Color' object has no attribute '{name}'")

for color_name in COLORS:
    setattr(_Color, color_name.lower(), property(lambda self, name=color_name: self.add_color(name)))

for style_name in STYLES:
    setattr(_Color, style_name.lower(), property(lambda self, name=style_name: self.add_style(name)))
