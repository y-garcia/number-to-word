class MajorSystem:

    def __init__(self):
        self._to_char = {
            '0': ['z', 's', 'x'],
            '1': ['t', 'd'],
            '2': ['n'],
            '3': ['m'],
            '4': ['r'],
            '5': ['l'],
            '6': ['j', 'g'],
            '7': ['k', 'c'],
            '8': ['f'],
            '9': ['b', 'p'],
            '': ['a', 'e', 'i', 'o', 'u', 'y', 'h']
        }
        self._to_digit = {}
        for number, chars in self._to_char.items():
            for char in chars:
                self._to_digit[char] = number
        self.count = 0

    def to_digit(self, char):
        return self._to_digit[char]

    def to_chars(self, digit):
        return self._to_char[str(digit)]

    def to_pattern(self, digit):
        return '[' + ''.join(self.to_chars(digit)) + ']'

    def get_silent_pattern(self):
        return '[' + ''.join(self.to_chars('')) + ']*'

    def build_pattern(self, number):
        vowels = self.get_silent_pattern()
        pattern = vowels
        for digit in list(number):
            pattern += self.to_pattern(digit) + vowels
        return f'^{pattern}$'
