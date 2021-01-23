class RoundElement:

    def __init__(self, elements):
        self.elements = elements.split()

    def convert_el_to_float(self):
        return map(float, self.elements)

    def round_elements(self):
        return [round(x) for x in self.convert_el_to_float()]


if __name__ == '__main__':
    test = RoundElement(input())
    print(test.round_elements())