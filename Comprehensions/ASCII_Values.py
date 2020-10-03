charackters = input().split(', ')

data = {}

for i in charackters:
    data[i] = ord(i)

print(data)

# a, b, c, a
# d, c, m, h