import re

def re_compile(regex, flags=0):
    """
    Return a compile regex object with the given flags.
    """
    if not isinstance(regex, str):
        raise TypeError('Regex must be and a str instace.')
    return re.compile(regex, flags=flags)