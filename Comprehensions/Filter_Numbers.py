start = int(input())
end = int(input())

result = [i for i in range(start, end + 1) if any(i % x == 0 for x in range(2, 10))]

print(result)