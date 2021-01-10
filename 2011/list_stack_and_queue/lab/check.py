# text = list("some text")
# result = []
#
# for i in text:
#     result.append(text.pop())

# print("".join(result))

# text = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
#
# brackets = []
#
# for i in range(len(text)):
#     if text[i] == '(':
#         brackets.append(i)
#     elif text[i] == ')':
#         start = brackets.pop()
#         print(text[start:i+1])

from collections import deque

# q = deque()
#
# while True:
#     command = input()
#     if command == 'Paid':
#         while q:
#             print(q.popleft())
#     elif command == 'End':
#         print(f"{len(q)} people remaining")
#         break
#     else:
#         q.append(command)


# quantity = int(input())
# q = deque()
#
# while True:
#     command = input()
#     if command == 'Start':
#         break
#     q.append(command)
#
#
# while True:
#     command2 = input()
#     if command2 == 'End':
#         print(f"{quantity} liters left")
#         break
#     elif command2.startswith('refill'):
#         quantity += int(command2.split()[1])
#     else:
#         if quantity >= int(command2):
#             quantity -= int(command2)
#             print(f"{q.popleft()} got water")
#         else:
#             print(f"{q.popleft()} must wait")


from collections import deque

childred = deque(input().split())
n = int(input())
index = 0

while len(childred) != 1:
    index += 1
    person = childred.popleft()
    if not index % n:
        print(f'Removed {person}')
    else:
        childred.append(person)

print(f'Last is {childred[0]}')
