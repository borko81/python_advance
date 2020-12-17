n = int(input())

odd = set()
even = set()

for _ in range(1, n + 1):
    name = input()
    acii_sum = sum([ord(x) for x in name])
    acii_sum = acii_sum // _
    if acii_sum % 2 == 0:
        even.add(acii_sum)
    else:
        odd.add(acii_sum)

if sum(odd) == sum(even):
    print(", ".join([str(x) for x in odd & even]))
elif sum(odd) > sum(even):
    print(", ".join([str(x) for x in odd - even]))
elif sum(odd) < sum(even):
    print(", ".join([str(x) for x in even ^ odd]))


