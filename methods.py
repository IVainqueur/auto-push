import re
from uuid import uuid4


colors_with_codes = {
    "black": "\x1B[30m",
    "bg-black": "\x1B[40m",
    "red": "\x1B[31m",
    "bg-red": "\x1B[41m",
    "green": "\x1B[32m",
    "bg-green": "\x1B[42m",
    "yellow": "\x1B[33m",
    "bg-yellow": "\x1B[43m",
    "blue": "\x1B[34m",
    "bg-blue": "\x1B[44m",
    "white": "\x1B[37m",
    "bg-white": "\x1B[47m",
    "clear": "\x1B[0m"
}

def param_dict(arr):
    classified = {}
    for el in arr:
        try:
            destructered = el.rsplit('=')
            if len(destructered) == 1:
                classified[destructered[0]] = True
            else:
                classified[destructered[0]] = destructered[1]

        except Exception as e:
            print(e)
    return classified

def colorcode(text, color, bg):
    if color not in colors_with_codes.keys():
        return f'{text}'

    if bg not in colors_with_codes.keys():
        return f'{colors_with_codes[color]}{text}{colors_with_codes["clear"]}'
    
    return f'{colors_with_codes[color]}{colors_with_codes[bg]}{text}{colors_with_codes["clear"]}'

def commit_message(template):
    if re.search("#num#", template):
        template = re.sub("#num#", uuid4().hex, template)
    else:
        template = f'{template}-{uuid4().hex}'
    return template
