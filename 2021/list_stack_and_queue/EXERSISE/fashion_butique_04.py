clothes = [int(x) for x in input().split()]
capacity = int(input())


class Fashion:
    def __init__(self, clothes, capacity: int):
        self.clothes = clothes
        self.capacity = capacity
        self.rack = 0
        self.counter = 0

    def get_capacity(self):
        while self.clothes:
            temp = self.clothes[-1]
            if self.counter + temp < capacity:
                self.counter += self.clothes.pop()
            else:
                self.rack += 1
                self.counter = 0

        if self.counter > 0:
            self.rack += 1
        return self.rack


if __name__ == '__main__':
    test = Fashion(clothes, capacity)
    print(test.get_capacity())
