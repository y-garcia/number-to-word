import re


def is_number(string):
    return re.match('\d', string)
