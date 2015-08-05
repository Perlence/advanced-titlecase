# -*- encoding: UTF-8 -*-
from __future__ import print_function

import re
import sys

FUNCTION_WORDS = """
the a an
for and nor but or yet so
to on of in from with at by vs as over

pour et ni ou mais pourtant si
à sur d'en partir avec au par vs

el las la
para y pero o sin embargo tan
desde con al por

die eine ein
für und noch oder aber doch so
auf der in aus mit von
""".split()

roman_pattern = re.compile(r"^M{0,4}"
                           r"(CM|CD|D?C{0,3})"
                           r"(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",
                           re.IGNORECASE)
pattern = re.compile(r"\w+('\w+)?", re.UNICODE)
sub_pattern = re.compile(r"(?<=[^,:-\\/] )\b({0})\b(?!( ?[\(\[])|\n|\.)"
                         .format("|".join(FUNCTION_WORDS)),
                         re.IGNORECASE | re.UNICODE)


def main():
    lines = sys.stdin.read()
    for line in lines.splitlines():
        cased = advanced_titlecase(line)
        print(cased)


def advanced_titlecase(string):
    string = titlecase(string)
    string = sub_pattern.sub(lambda mo: "{0}".format(mo.group(1).lower()),
                             string)
    return string


def titlecase(string):
    def f(mo):
        roman_mo = roman_pattern.match(mo.group())
        if roman_mo:
            return mo.group().upper()
        else:
            return (mo.group(0)[0].upper() + mo.group(0)[1:].lower())
    return pattern.sub(f, string)

if __name__ == '__main__':
    main()
