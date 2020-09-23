n = int(input())

odd = set()
even = set()

for line in range(1, n + 1):
    name = input()
    number = sum([ord(i) for i in name]) // line
    if number & 1:
        odd.add(number)
    else:
        even.add(number)

if sum(odd) == sum(even):
    print(", ".join(str(x) for x in (even | odd)))
elif sum(odd) > sum(even):
    print(", ".join(str(x) for x in (odd - even)))
else:
    print(", ".join(str(x) for x in (even ^ odd)))
