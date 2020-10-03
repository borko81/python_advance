numbers = [int(x) for x in input().split(', ')]

print(f'Positive: {", ".join([str(i) for i in numbers if i >= 0])}')
print(f'Negative: {", ".join([str(i) for i in numbers if i < 0])}')
print(f'Even: {", ".join([str(i) for i in numbers if i % 2 == 0])}')
print(f'Odd: {", ".join([str(i) for i in numbers if i & 1])}')