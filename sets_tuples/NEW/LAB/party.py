num = int(input())


def push_in_data():
    result = []
    for _ in range(num):
        line = input()
        result.append(line)
    return result


result = push_in_data()

while True:
    line = input()
    if line == 'END':
        break

    result.pop(result.index(line))


print(len(result))
[print(x) for x in sorted(result)]