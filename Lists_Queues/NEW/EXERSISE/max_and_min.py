query= int(input())

result = []

for _ in range(query):
    number = input()

    if len(number.split()) == 2:
        _, n = number.split()
        n = int(n)
        result.append(n)

    else:
        number = int(number)
        if number == 2 and len(result) > 0:
            result.pop()

        elif number == 3 and len(result) > 0:
            print(max(result))

        elif number == 4 and len(result) > 0:
            print(min(result))


result = list(reversed(result))
print(", ".join((str(x) for x in result)))