from collections import deque


class Restaurant:

    def __init__(self, quantity: int):
        self.quantity = int(quantity)
        self.clients = deque()

    def add_client(self):
        for client in [int(x) for x in input().split()]:
            self.clients.append(client)

    def find_biggest_order(self):
        return max(self.clients)

    def is_completed(self):
        finish = True
        while self.clients:
            check = self.clients[0]
            if self.quantity >= check:
                self.quantity -= self.clients.popleft()
            else:
                print(f'Orders left: {" ".join(str(x) for x in self.clients)}')
                finish = False
                break
        if finish:
            print('Orders complete')


test = Restaurant(input())
test.add_client()
print(test.find_biggest_order())
test.is_completed()





