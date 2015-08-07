# -*- encoding: UTF-8 -*-
from __future__ import print_function

import re
import sys

FUNCTION_WORDS = u"""
the a an
for and nor but or yet so
to on of in from with at by vs as over

pour et ni ou mais pourtant si
à sur d'en partir avec au par vs

el las la
para y pero sin embargo tan
desde con al por

die eine ein
für und noch oder aber doch so
auf der in aus mit von
""".split()

ROMAN_PATTERN = re.compile(ur"^M{0,4}"
                           ur"(CM|CD|D?C{0,3})"
                           ur"(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",
                           re.IGNORECASE | re.UNICODE)
PATTERN = re.compile(ur"\w+('\w+)?", re.UNICODE)


def main():
    lines = sys.stdin.read()
    for line in lines.splitlines():
        cased = advanced_titlecase(line)
        print(cased)


def advanced_titlecase(string):
    """Titlecase all words and lowercase selected function words."""
    string = titlecase(string)
    words = string.split()
    contexts = zip([None] + words, words + [None])
    result = []
    for left, word in contexts:
        if word is None:
            continue
        lower = word.lower()
        if (left is not None and
                lower in FUNCTION_WORDS and
                re.search(ur"[\]\)\-:.]$", left) is None):
            result.append(lower)
        else:
            result.append(word)
    return ' '.join(result)


def titlecase(string):
    """Titlecase all words in the string.

    Words with quote (') titlecased only in the beginning, as opposed to
    built-in ``str.title()``. Roman numerals are uppercased.
    """
    def f(mo):
        roman_mo = ROMAN_PATTERN.match(mo.group())
        if roman_mo:
            return mo.group().upper()
        else:
            return (mo.group(0)[0].upper() + mo.group(0)[1:].lower())
    return PATTERN.sub(f, string)

if __name__ == '__main__':
    main()
