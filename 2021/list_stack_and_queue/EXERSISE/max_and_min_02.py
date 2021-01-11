class MaxAndMin:

    def __init__(self, num):
        self.arr = []
        for i in range(int(num)):
            command = [int(x) for x in input().split()]
            if len(command) == 2:
                self.arr.append(command[1])
            elif command[0] == 2:
                self.delete()
            elif command[0] == 3:
                self.maximum()
            elif command[0] == 4:
                self.minimum()

    def push(self, element):
        self.arr.append(element)

    def delete(self):
        try:
            self.arr.pop()
        except:
            pass

    def maximum(self):
        print(max(self.arr))

    def minimum(self):
        print(min(self.arr))



test = MaxAndMin(input())
print(", ".join([str(x) for x in test.arr[::-1]]))


