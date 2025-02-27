RESET = "\033[0m"

STYLES = {
    'BOLD': '1',
    'ITALIC': '3',
    'UNDERLINE': '4',
    'NORMAL': '0'
}

COLORS = {
    'RED': '31',
    'GREEN': '32',
    'YELLOW': '33',
    'BLUE': '34',
    'MAGENTA': '35',
    'CYAN': '36',
    'WHITE': '37',
    'BRIGHT_RED': '91',
    'BRIGHT_GREEN': '92',
    'BRIGHT_YELLOW': '93',
    'BRIGHT_BLUE': '94',
    'BRIGHT_MAGENTA': '95',
    'BRIGHT_CYAN': '96',
    'BRIGHT_WHITE': '97',
}

REGEX_HEX = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
REGEX_RGB = r'^\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$'
