from itertools import groupby

from .exceptions import WrongLengthException, UnicodeException, \
    EmptyStringError


def translation(first, second):
    """Create an index of mapped letters (zip to dict)."""
    if len(first) != len(second):
        raise WrongLengthException('The lists are not of the same length!')
    return dict(zip(first, second))


def squeeze(word):
    """Squeeze the given sequence by dropping consecutive duplicates."""
    return ''.join(x[0] for x in groupby(word))


def check_str(word):
    """Throw exception at non-string input."""
    if not isinstance(word, str):
        raise UnicodeException('Expected a unicode string!')


def check_empty(word):
    """Throw exception at empty string input."""
    if not len(word):
        raise EmptyStringError('The given string is empty.')

class LazyString(str):
    def get(self, idx, dist=None):
        if not self:
            return None
        if idx < 0 or idx >= len(self):
            return None
        if dist:
            if idx + dist > len(self):
                return None
            return self[idx:idx+dist]
        return self[idx]


def startswith(word, matchwith):
    return all(map(lambda x: x[0] == x[1], zip(word, matchwith)))


def endswith(word, matchwith):
    return all(map(lambda x: x[0] == x[1], zip(word[::-1], matchwith[::-1])))


def isvowel(c):
    return c and c.upper() in {'A', 'E', 'I', 'O', 'U', 'Y'}


def isslavogermanic(s):
    if not s:
        return False
    s = s.upper()
    return "W" in s or "K" in s or "CZ" in s or "WITZ" in s