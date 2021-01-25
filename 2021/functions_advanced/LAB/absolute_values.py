class AbsoluteValues:
    def __init__(self, args):
        self.val = args.split()

    def read_values(self):
        return map(float, self.val)

    def return_abs_values(self):
        return [abs(x) for x in self.read_values()]

    def __repr__(self):
        return self.val


test = AbsoluteValues(input())
print(test.return_abs_values())