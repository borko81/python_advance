start = int(input())
end = int(input())

result = [x for x in range(start, end + 1) if any(x % i == 0 for i in range(2, 11))]

print(result)