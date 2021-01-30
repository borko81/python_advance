def list_manipulator(nums, *args):
    numbers = nums.copy()

    if args[0] == "add" and args[1] == "beginning":
        numbers[0:0] = list(args[2:])

    elif args[0] == "add" and args[1] == "end":
        numbers.extend(args[2:])

    elif args[0] == 'remove' and args[1] == 'beginning' and len(args) == 2:
        numbers.pop(0)

    elif args[0] == 'remove' and args[1] == 'beginning' and len(args) > 2:
        numbers = numbers[args[2]:]

    elif args[0] == 'remove' and args[1] == 'end' and len(args) == 2:
        numbers.pop()

    elif args[0] == 'remove' and args[1] == 'end' and len(args) > 2:
        numbers = numbers[:len(numbers) - args[2]]

    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([11, 22, 33], "remove", "end", 0))
print(list_manipulator([1, 2, 3], "remove", "beginning", 1))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
