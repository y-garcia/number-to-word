class MajorSystem:

    def __init__(self):
        self._to_char = {
            '0': ['z', 's', 'x', 'c'],
            '1': ['t', 'd'],
            '2': ['n', 'ñ'],
            '3': ['m'],
            '4': ['r'],
            '5': ['l'],
            '6': ['j', 'g'],
            '7': ['k', 'c', 'q'],
            '8': ['f'],
            '9': ['b', 'p', 'v'],
            '': ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w', 'á', 'é', 'í', 'ó', 'ú', 'ü']
        }

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
