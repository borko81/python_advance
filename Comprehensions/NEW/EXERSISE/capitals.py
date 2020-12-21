country = input().split(', ')
capitals = input().split(', ')

[print(" -> ".join(x)) for x in zip(country, capitals)]
