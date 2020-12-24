class RomanNumberConvert:
    def __init__(self):
        self.digit_map = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

    def convert_to_decimal(self, roman_number):
        val = 0

        for char in roman_number:
            val += self.digit_map[char]

        return val


if __name__ == '__main__':
    test = RomanNumberConvert()
    print(test.convert_to_decimal('LI'))