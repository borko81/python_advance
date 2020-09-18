n = int(input())

stack = []

for _ in range(n):
    line = input().split()
    command = int(line[0])
    if int(command) == 1:
        stack.append(line[1])

    elif command == 2:
        if len(stack) > 0:
            stack.pop()
    elif command == 3 and len(stack) > 0:
            print(max(stack))
    elif command == 4 and len(stack) > 0:
            print(min(stack))


print(", ".join(str(i) for i in reversed(stack)))