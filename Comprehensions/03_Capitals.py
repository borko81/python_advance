countries = input().split(', ')
cites = input().split(', ')

for x, y in zip(countries, cites):
    print('{country} -> {capital}'.format(country=x, capital=y))