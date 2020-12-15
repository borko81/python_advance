input_string = input().split()
result = []

while input_string:
    result.append("".join(reversed(input_string.pop())))

print(" ".join(result))