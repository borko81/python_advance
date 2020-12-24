class Employee:
    """A sample employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


if __name__ == '__main__':
    test = Employee('Boris', 'St', 1500)
    print(test.email)
    test.apply_raise()
    print(test.pay)