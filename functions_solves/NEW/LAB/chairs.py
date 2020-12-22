names = input().split(', ')
size = int(input())

def chair(names, size, result=[]):
    if len(result) == size:
        print(", ".join(result))
        return
    for i in range(len(names)):
        name = names[i]
        result.append(name)
        chair(names[i+1:], size, result)
        result.pop()

chair(names, size)