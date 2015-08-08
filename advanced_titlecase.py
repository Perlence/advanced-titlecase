# -*- encoding: UTF-8 -*-
from __future__ import print_function

import re
import sys

FUNCTION_WORDS = u"""
the a an
for and nor but or yet so
to on of in from with at by vs as over
cum mid off per qua re up via

pour et ni ou mais pourtant si
sur d'en partir avec au par vs

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
ENDS_WITH_PUNCTUATION = re.compile(ur"[\]\)\-~/:.?!]$", re.UNICODE)
STARTS_WITH_PUNCTUATION = re.compile(ur"^[\[\(\-~/]", re.UNICODE)


def main():
    lines = sys.stdin.read()
    for line in lines.splitlines():
        cased = advanced_titlecase(line)
        print(cased)


def advanced_titlecase(string):
    """Capitalize English titles."""
    string = titlecase(string)
    words = string.split()
    contexts = zip([None, None] + words,
                   [None] + words + [None],
                   words + [None, None])
    result = []
    for left, word, right in contexts:
        if word is None:
            continue
        lower = word.lower()
        stripped = lower.strip('.')
        if ((left is not None and
                right is not None and
                lower in FUNCTION_WORDS and
                ENDS_WITH_PUNCTUATION.search(left) is None and
                STARTS_WITH_PUNCTUATION.search(right) is None) or
                (stripped in FUNCTION_WORDS and
                 (lower.startswith('..') or lower.endswith('..')))):
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

        word = mo.group(0)
        tail = word[1:]
        tail_lower = tail.lower()
        # If the tail of the word is uppercase then leave it as is.
        if tail_lower != tail:
            return word

        return (word[0].upper() + tail_lower)
    return PATTERN.sub(f, string)

if __name__ == '__main__':
    main()
