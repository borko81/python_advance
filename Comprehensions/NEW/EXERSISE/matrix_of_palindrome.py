row = int(input())
cols = int(input())

a = ord('a')


for r in range(row):
    for c in range(cols):
        print(f"{chr(a + r)}{chr(a+r+c)}{chr(a+r)}" , end=' ')
    print()