numbers = [int(x) for x in input().split(', ')]

# Not use map, becouse numbers become iterator!

print("Positive: " + ", ".join([str(x) for x in numbers if x >= 0]))
print("Negative: " + ", ".join([str(x) for x in numbers if x < 0]))
print("Even: " + ", ".join([str(x) for x in numbers if x % 2 == 0]))
print("Odd: " + ", ".join([str(x) for x in numbers if x&1]))